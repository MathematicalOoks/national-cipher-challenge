class Affine:
    def modInverse(self, a, m):
        for x in range(1, m):
            if (a * x) % m == 1:
                return x
        return -1

    def decrypt(self, text):
        m = 26 
        plaintext = ""

        for a in range(1, 27):
            for b in range(0, 26):
                inverse = self.modInverse(a, m)
                if inverse == -1:
                    continue
                
                plaintext = ""
                for i in text:
                    if 'A' <= i <= 'Z':
                        decrypted_char = (inverse * ((ord(i) - 65) - b)) % m
                        plaintext += chr(decrypted_char + 65)
                    else:
                        plaintext += i

                if "@" not in plaintext:
                    print(plaintext, '\n')
