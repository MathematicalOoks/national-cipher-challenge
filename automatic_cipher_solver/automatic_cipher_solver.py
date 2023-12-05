from random import shuffle

class CipherSolver():
    def __init__(self, ciphertext, scoring_function, decrypt_function, parent_key1, parent_key2, child_key_generator):
        self.ciphertext = ciphertext
        self.scoring_function = scoring_function
        self.decrypt_function = decrypt_function
        self.parent_key1 = parent_key1
        self.parent_key2 = parent_key2
        self.child_key_generator = child_key_generator
        self.__tmp_keys = []
    
    def __return_sorted_fittest_key(self, *args):
        return sorted(args, key=lambda x: -self.scoring_function(self.decrypt_function(x, self.ciphertext)))

    def __return_fittest_key(self, *args):
        return self.__return_sorted_fittest_key(*args)[0]

    def __check_keys_have_changed(self, *args):
        if self.__tmp_keys != args:
            self.__tmp_keys = args
            return True
        return False

    def return_best_key(self, iterations = 100, mutation_cutoff = 1000):
        best_score, best_key = -999999999999, ""
        for i in range(iterations):
            child_key = self.child_key_generator(self.parent_key1, self.parent_key2, self.__return_fittest_key)
            if self.__return_sorted_fittest_key(self.parent_key1, self.parent_key2, child_key)[0] == child_key:
                self.parent_key1, self.parent_key2 = child_key, self.parent_key1
            else:
                self.parent_key1, self.parent_key2 = self.parent_key2, child_key
            

            if self.scoring_function(self.decrypt_function(self.parent_key1, self.ciphertext)) > best_score:
                best_key = self.parent_key1
                best_score = self.scoring_function(self.decrypt_function(best_key, self.ciphertext))
                print(f"The current score is {best_score} and the decrypted ciphertext is {''.join(self.decrypt_function(best_key, self.ciphertext)).lower()}, the current key is {''.join(best_key)}")
        return self.__return_fittest_key(self.parent_key1, self.parent_key2)

