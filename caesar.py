class Caesar:

    def decrypt(self, text):
        plaintext = ""
        char = text[0]
        Map = {}
        for i in text:
            if 'A' <= i <= 'Z':
                if i not in Map:
                    Map[i] = 1
                else:
                    Map[i] += 1

                if Map[i] > Map[char]:
                    char = i

        diff = ord('E') - ord(char)

        for i in text:
            if 'A' <= i <= 'Z':
                if ord(i) + diff < ord('A'):
                    plaintext += chr(ord('Z') + diff + ord(i) - ord('A'))
                elif ord(i) + diff > ord('Z'):
                    plaintext += chr(ord('A') + diff - (ord('Z') - ord(i) + 1))
                else:
                    plaintext += chr(ord(i) + diff)
            else:
                plaintext += i

        return plaintext
