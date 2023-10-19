alphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')


class Vignere:

    def generateKey(self, text, keyword):
        key = list(keyword)
        if len(text) == len(key):
            return key
        else:
            for i in range(len(text) - len(key)):
                key.append(key[i % len(key)])
        return "".join(key)

    def decryption(self, text, key):
        plain_text = []
        for i in range(len(text)):
            if text[i].lower() in alphabet:
                x = (ord(text[i]) - ord(key[i]) + 26) % 26
                x += ord('A')
                plain_text.append(chr(x))
            else:
                plain_text.append(text[i])
        return "".join(plain_text)

    def findBestKeyLength(self, text):
        english_ioc = 0.067
        uniform_random_selection = 0.0385
        ioc = self.indexOfCoincidence(text)
        print(ioc)
        return round((english_ioc - uniform_random_selection) / (ioc - uniform_random_selection))

    def indexOfCoincidence(self, text):
        index = 0
        frequency = {}
        compressed_cipher_text = ""
        for i in text:
            if i.lower() in alphabet:
                compressed_cipher_text += i
        for i in compressed_cipher_text:
            if i in frequency:
                frequency[i] += 1
            else:
                frequency[i] = 1
        for i in frequency:
            index += frequency[i] * (frequency[i] - 1) / (
                    len(compressed_cipher_text) * (len(compressed_cipher_text) - 1))
        return index
