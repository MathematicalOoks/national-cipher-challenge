def return_best_key(self, iterations = 100, score_cutoff = -999999999999):
        best_score = max(-999999999999, score_cutoff)
        best_key = ""
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
