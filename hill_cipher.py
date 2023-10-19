import itertools


class HillCipher:
    def __init__(self):
        possibleValues = list(range(26))

        # Generate all possible 2x2 key matrices using itertools.product
        self.possibleMatrices = list(itertools.product(possibleValues, repeat=4))

    def decrypt(self, ciphertext, n, key=None):
        splitText = [[]]
        decryptions = []
        for i in ciphertext:
            if 'A' <= i <= 'Z':
                splitText[-1].append(ord(i) - 65)
                if len(splitText[-1]) == n:
                    splitText.append([])

        numberOfPads = n - len(splitText[-1])
        if len(splitText[-1]) != n:
            for i in range(numberOfPads):
                splitText[-1].append(-1)

        for keyMatrix in self.possibleMatrices:
            decryption_attempt = []

            for block in splitText:
                # Create a 2x2 matrix from the key_matrix
                key = [[keyMatrix[0], keyMatrix[1]], [keyMatrix[2], keyMatrix[3]]]

                # Perform matrix multiplication for decryption
                decrypted_block = [
                    (key[0][0] * block[0] + key[0][1] * block[1]) % 26,
                    (key[1][0] * block[0] + key[1][1] * block[1]) % 26
                ]

                decryption_attempt.extend(decrypted_block)

            # Convert numerical values back to characters
            decrypted_text = ''.join(chr(i + 65) for i in decryption_attempt if i >= 0)[
                             :len(decryption_attempt) - numberOfPads]
            decryptions.append(decrypted_text)

        return decryptions
