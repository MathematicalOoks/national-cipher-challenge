import string
from collections import Counter


class EnglishDetector:

    def isEnglish(self, text, cribs=set()):
        # Step 1: Calculate letter frequencies
        text = text.upper()  # Convert to uppercase for consistency
        letterFreq = Counter(c for c in text if 'A' <= c <= 'Z')

        # Step 2: Check for cribs
        cribFound = False
        for crib in cribs:
            if crib in text:
                cribFound = True
                break

        # Step 3: Check letter frequencies against English
        expected_freq = {'E': 12.02, 'T': 9.10, 'A': 8.12, 'O': 7.68, 'I': 7.31}
        chi_square_threshold = 10  # Adjust as needed
        chi_square = sum(((letterFreq[c] - expected_freq[c]) ** 2) / expected_freq[c] for c in string.ascii_uppercase)
        if chi_square < chi_square_threshold and cribFound:
            return True  # Likely English

        return False  # Not likely English
