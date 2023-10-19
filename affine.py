class Affine:

    def modInverse(self, a, m):

        for x in range(1, m):
            if (a % m) * (x % m) % m == 1:
                return x
        return -1

    def decrypt(self, text):
        a = 1
        b = 1
        plaintext = ""

        while a < 27:
            while b < 27:
                for i in text:
                    if 'A' <= i <= 'Z':
                        inverse = self.modInverse(a, 26)
                        if inverse != -1:
                            plaintext += chr(64+(inverse*(ord(i)-64-b)) % 26)
                        else:
                            plaintext += i
                    else:
                        plaintext += i
                b += 1
                if "@" not in plaintext:
                    print(plaintext)
                plaintext = ""
            a += 1
            b = 1
            plaintext = ""
