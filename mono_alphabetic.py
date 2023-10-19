from collections import Counter


class MonoAlphabetic:

    def __init__(self):
        self.sortedFrequencies = [
            'E', 'T', 'A', 'O', 'I', 'N', 'S', 'H', 'R', 'D', 'L', 'U', 'C', 'M',
            'W', 'F', 'G', 'Y', 'P', 'B', 'V', 'K', 'J', 'X', 'Q', 'Z'
        ]

    def decrpyt(self, ciphertext, key=None):
        if key is None:
            frequencies = Counter(ciphertext)
            uppercaseFrequencies = dict(
                sorted({char: count for char, count in frequencies.items() if 'A' <= char <= 'Z'}.items(),
                       key=lambda item: item[1],
                       reverse=True))
            key = {char: self.sortedFrequencies[index] for index, char in enumerate(uppercaseFrequencies)}

        plainText = ''.join(key[i] if 'A' <= i <= 'Z' else i for i in ciphertext)

        return plainText
