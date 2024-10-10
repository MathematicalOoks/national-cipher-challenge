class Caesar:
    def decrypt(self, text):
        plaintext = ""
        frequency_map = {}
        
        for i in text:
            if 'A' <= i <= 'Z':
                if i not in frequency_map:
                    frequency_map[i] = 1
                else:
                    frequency_map[i] += 1

        if frequency_map:
            most_frequent_letter = max(frequency_map, key=frequency_map.get)
        else:
            return text

        shift = ord(most_frequent_letter) - ord('E')

        for i in text:
            if 'A' <= i <= 'Z':
                decrypted_char = chr((ord(i) - shift - 65) % 26 + 65)
                plaintext += decrypted_char
            else:
                plaintext += i

        return plaintext
