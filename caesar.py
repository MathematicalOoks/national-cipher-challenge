baseAlphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
class Caesar:
    def __init__(self, text):
        self.text = text
        self.frequent = 'e'
        self.map = {}

    def decode(self):
        res = ""
        maximum = 0
        char = ''
        for i in self.text:
            if i not in baseAlphabet:
                if i in self.map.keys():
                    self.map[i] = self.map.get(i)+1
                else:
                    self.map[i] = 1
                if self.map[i] > maximum:
                    char = i
                    maximum = self.map[i]
        diff = ord(self.frequent)-ord(char.lower())
        for i in self.text:
            if i not in baseAlphabet:
                res += i
            else:
                if ord(i.lower()) + diff < 97:
                    res += chr(123-(abs(diff)-(ord(i.lower())-97)))
                elif ord(i.lower()) + diff > 122:
                    res += chr(96+diff)
                else:
                    res += chr(ord(i.lower())+diff)
        return res
