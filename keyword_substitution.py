class Keyword:

    def convertKey(self, key):
        finalKey = ""
        val = set()

        for i in key:
            if i not in val:
                finalKey += i
            val.add(i)

        return finalKey

    def decrypt(self, ciphertext, key):
        key = self.convertKey(key)
        keyMap = {}
        currSet = set()
        alphabet = []

        for i in key:
            currSet.add(i)

        for i in range(26):
            if chr(i + 65) not in currSet:
                alphabet.append(chr(i + 65))

        for i in range(len(key)):
            keyMap[key[i]] = chr(i + 65)

        for i in range(len(alphabet)):
            keyMap[alphabet[i]] = chr(i + len(key) + 65)

        plaintext = ""

        for i in ciphertext:
            if 'A' <= i <= 'Z':
                plaintext += keyMap[i]
            else:
                plaintext += i

        if plaintext.find("MAURICE") != -1:
            return plaintext

        return ""
