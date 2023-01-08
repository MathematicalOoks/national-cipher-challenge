alphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

class Vignere:
    def __init__(self, cipher_text):
        self.cipher_text = cipher_text
        self.plain_text = ""
        
    def generate_key(self, keyword):
        key = list(keyword)
        if len(self.cipher_text) == len(key):
            return key
        else:
            for i in range(len(self.cipher_text) - len(key)):
                key.append(key[i % len(key)])
        return "".join(key)
    
    def decryption(self, key):
        plain_text = []
        for i in range(len(self.cipher_text)):
            if self.cipher_text[i].lower() in alphabet:
                x = (ord(self.cipher_text[i]) - ord(key[i]) + 26) % 26
                x += ord('A')
                plain_text.append(chr(x))
            else:
                plain_text.append(self.cipher_text[i])
        return "".join(plain_text)
        
    def find_best_key_length(self):
        english_ioc = 0.067
        uniform_random_selection = 0.0385
        ioc = self.index_of_coincidence()
        print(ioc)
        return round((english_ioc - uniform_random_selection)/(ioc - uniform_random_selection))
    
    def index_of_coincidence(self):
        index = 0
        frequency = {}
        compressed_cipher_text = ""
        for i in self.cipher_text:
            if i.lower() in alphabet:
                compressed_cipher_text += i
        for i in compressed_cipher_text:
            if i in frequency:
                frequency[i] += 1
            else:
                frequency[i] = 1
        for i in frequency:
            index += frequency[i]*(frequency[i]-1)/(len(compressed_cipher_text)*(len(compressed_cipher_text)-1))
        return index
