lower_case_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                       'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper_case_alphabet = alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
                                  'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
key_length = 5
keys = []


def generate_all_k_length(chars, k):
    print_all_k_length_rec(chars, "", len(chars), k)


def print_all_k_length_rec(chars, prefix, n, k):
    if k == 0:
        keys.append(prefix)
        return

    for i in range(n):
        new_prefix = prefix + chars[i]
        print_all_k_length_rec(chars, new_prefix, n, k - 1)


generate_all_k_length(upper_case_alphabet, key_length)
print(keys)
