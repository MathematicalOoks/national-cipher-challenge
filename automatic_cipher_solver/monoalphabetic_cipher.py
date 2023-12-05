from string import ascii_uppercase
from collections import Counter
from random import randint, shuffle

def decrypt_monoalphabetic(key, ciphertext):
    assert set(key) <= set(ascii_uppercase)
    assert set(ciphertext) <= set(ascii_uppercase)
    assert len(key) == 26
    assert len(key) == len(set(key))
    mapping = {ascii_uppercase[i]:key[i] for i in range(26)}
    plaintext = []
    return [mapping[letter] for letter in ciphertext]


def generate_valid_starting_key(ciphertext):
    assert set(ciphertext) <= set(ascii_uppercase)
    natural_frequency = "ETAOINSHRDLUCMWFGYPBVKJXQZ"
    ciphertext_frequencies = Counter(ciphertext)
    for letter in ascii_uppercase:
        if letter not in ciphertext_frequencies:
            ciphertext_frequencies[letter] = 0
    ciphertext_ordered_frequencies = ciphertext_frequencies.most_common()
    key = [""] * 26
    for i in range(26):
        key[i] = ciphertext_ordered_frequencies[i][0]
    return key

def generate_random_valid_starting_key(ciphertext):
    key = list(ascii_uppercase)
    shuffle(key)
    return key


def generate_child_key(parent1, parent2, fittest_key_function):
    assert type(parent1) == list
    assert type(parent2) == list
    fitter_key = fittest_key_function(parent1, parent2)[:]
    assert type(fitter_key) == list
    less_fit_key = parent1 if fittest_key_function(parent1, parent2) == parent2 else parent2
    less_fit_key = less_fit_key[:]
    for i in range(26):
        if fitter_key[i] == less_fit_key[i]:
            continue
        else:
            for j in range(26):
                tmp_key = fitter_key[:]
                tmp_key[i], tmp_key[j] = tmp_key[j], tmp_key[i]
                fitter_key = fittest_key_function(fitter_key, tmp_key)
    for i in range(3):
        i = randint(0,25)
        j = randint(0,25)
        fitter_key[i], fitter_key[j] = fitter_key[j], fitter_key[i]
    return fitter_key


if __name__ == "__main__":
    #print(decrypt_monoalphabetic("HBCDEFGAIJKLMNOPQRSTUVWXYZ", "HELLOFROMTHEOTHERSIDE"))
    print(generate_valid_starting_key("HELLOFROMTHEOTHERSIDE"))
