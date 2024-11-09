def decrypt(text, key):
    plain_text = []
    key_index = 0

    for i in range(len(text)):
        if 'A' <= text[i] <= 'Z':
            x = (ord(text[i]) - ord(key[key_index]) + 26) % 26
            x += ord('A')
            plain_text.append(chr(x))
            key_index = (key_index + 1) % len(key)
        else:
            plain_text.append(text[i])

    return "".join(plain_text)

def findBestKeyLength(text):
    english_ioc = 0.067
    uniform_random_selection = 0.0385
    ioc = indexOfCoincidence(text)
    return round((english_ioc - uniform_random_selection) / (ioc - uniform_random_selection))

def indexOfCoincidence(text):
    index = 0
    frequency = {}
    compressed_cipher_text = ""
    for i in text:
        if 'A' <= i <= 'Z':
            compressed_cipher_text += i
    for i in compressed_cipher_text:
        if i in frequency:
            frequency[i] += 1
        else:
            frequency[i] = 1
    for i in frequency:
        index += frequency[i] * (frequency[i] - 1) / (
                len(compressed_cipher_text) * (len(compressed_cipher_text) - 1))
        
    return index
