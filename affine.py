baseAlphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
class Affine:
    def __init__(self, text):
        self.text = text

    def mod_inv(self, a, m):

        for x in range(1, m):
            if (a % m) * (x % m) % m == 1:
                return x
        return -1

    def decode(self):
        a = 1
        b = 1
        inv = -1
        res = ""
        while a < 27:
            while b < 27:
                for i in self.text:
                    if i.lower() in baseAlphabet:
                        inv = self.mod_inv(a, 26)
                        if inv != -1:
                            res += chr(64+(inv*(ord(i)-64-b)) % 26)
                        else:
                            res += i
                    else:
                        res += i
                b += 1
                if "@" not in res:
                    print(res)
                res = ""
            a += 1
            b = 1
            res = ""
