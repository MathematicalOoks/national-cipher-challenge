class RailFence:

    # Assume spaces are given in ciphertext
    def decrypt(self, ciphertext):
        plaintext = ""
        text = ciphertext.split(' ')
        lengthOfText = len(ciphertext) - ciphertext.count(' ')
        charsProcessed = 0
        direction = 1
        columnMap = {i: 0 for i in range(len(text))}

        while charsProcessed != lengthOfText:
            if direction == 1:
                for i in range(len(text)):
                    if columnMap[i] < len(text[i]):
                        plaintext += text[i][columnMap[i]]
                        columnMap[i] += 1
                        charsProcessed += 1
            else:
                for i in range(len(text)-2, 0, -1):
                    if columnMap[i] < len(text[i]):
                        plaintext += text[i][columnMap[i]]
                        columnMap[i] += 1
                        charsProcessed += 1

            direction *= -1

        return plaintext
