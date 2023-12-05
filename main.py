DEBUG = False


from ciphertext_scorer import CipherTextScorer
from automatic_cipher_solver import CipherSolver

from monoalphabetic_cipher import decrypt_monoalphabetic, generate_valid_starting_key, generate_child_key, generate_random_valid_starting_key

if DEBUG:
    from cProfile import run



ciphertext = "KVELPAFOECSOEMLFMBODAELYEZALODSPAXAALKMTABTREOBRHODSLEYMRHZDSPADMNAZNELGATOMLFDSPANTMPEZAZYHASTAPEZALYAODSOODATAQSFSYMLFNETSYVOMFOASHBTMKKVHEXTSTVSLZODSOAPEZALYANMELOFOMKVAKNHMVATMTSOHASFOFMKAMLAELDEFAKNHMVKALOKTTMCATFDSZNHSLLAZOMZMLSOAODAYMHHAYOEMLO"

print("loading the ngram file")
scorer = CipherTextScorer(4)
scorer.load_ngram_file("quadgrams.txt")
print("the ngram file is done loading")

def custom_scoring(plaintext):
    base_score = scorer.calculate_score(plaintext)
    return base_score


parent_key1 = generate_random_valid_starting_key(ciphertext)
parent_key2 = generate_random_valid_starting_key(ciphertext)

solver = CipherSolver(ciphertext, custom_scoring, decrypt_monoalphabetic, 
parent_key1, parent_key2, generate_child_key)
best_key = ""


def main():solver.return_best_key(iterations=10000000)

if DEBUG:
    run("main()")
else:
    main()