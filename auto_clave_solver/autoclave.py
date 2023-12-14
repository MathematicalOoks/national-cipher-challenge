class AutoClave:

    def generateKeyStream(self, plaintext, key):
        return key + plaintext

    def encryption(self, plaintext, keystream):
        ciphertext = ""

        for i in range(len(plaintext)):
            calculation = (ord(plaintext[i]) + ord(keystream[i]) - 130) % 26
            ciphertext += chr(calculation + 65)

        return ciphertext

    def decryption(self, text, key):
        plain_text = []

        for i in range(len(text)):
            if 'A' <= text[i] <= 'Z':
                x = (ord(text[i]) - ord(key[i]) + 26) % 26
                x += ord('A')
                key.append(chr(x))
                plain_text.append(chr(x))
            else:
                plain_text.append(text[i])

        return "".join(plain_text)
