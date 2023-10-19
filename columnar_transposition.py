class ColumnarTransposition:

    def decrypt(self, ciphertext, key):
        grid = ''.join(ciphertext.split(' '))
        splitText = [[]]
        numRows = len(grid) // len(key)

        # Add extra row if length of ciphertext is not a multiple of the key length
        if len(grid) % len(key) == 0:
            lastRow = numRows
        else:
            lastRow = numRows + len(grid) % len(key)

        currRows = 0

        # Split the grid into columns (which will be moved)
        for i in range(len(grid) - lastRow):
            currRows += 1
            splitText[-1].append(grid[i])
            if currRows % numRows == 0:
                splitText.append([])

        # Special loop for last column as more elements may be contained
        for i in range(len(grid) - lastRow, len(grid)):
            splitText[-1].append(grid[i])

        # Generate map for columns
        sortedKey = ''.join(sorted(key))
        charMap = {}
        columnMap = {}

        for i in range(len(key)):
            charMap[key[i]] = i

        for i in range(len(key)):
            columnMap[i] = charMap[sortedKey[i]]

        plaintext = [[''] * len(key) for _ in range(lastRow)]

        for column in range(len(splitText)):
            newColumn = columnMap[column]
            for j in range(len(splitText[column])):
                plaintext[j][newColumn] = splitText[column][j]

        stringPlainText = ""
        for row in plaintext:
            stringPlainText += ''.join(row)

        return stringPlainText

    def doubleTransposition(self, ciphertext, key):
        secondCiphertext = self.decrypt(ciphertext, key)
        plaintext = self.decrypt(secondCiphertext, key)
        return plaintext
