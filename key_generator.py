class KeyGenerator:

    def __init__(self):
        self.keys = []
        self.lowerCaseAlphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                                  'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        self.upperCaseAlphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
                                  'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    def generateAllKlength(self, chars, k):
        self.printAllKlengthRec(chars, "", len(chars), k)
        return self.keys

    def printAllKlengthRec(self, chars, prefix, n, k):
        if k == 0:
            self.keys.append(prefix)
            return

        for i in range(n):
            new_prefix = prefix + chars[i]
            self.printAllKlengthRec(chars, new_prefix, n, k - 1)
