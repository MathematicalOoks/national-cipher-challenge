from string import ascii_uppercase
from math import log

try:
   from more_itertools import sliding_window
   print("more_itertools successfully loaded")
except ImportError:
    print("To use sliding_window, more-itertools must be installed from pip")
    print("A slower alternative is provided here from itertools documentation")
    from collections import deque
    from itertools import islice
    def sliding_window(iterable, n):
        # sliding_window('ABCDEFG', 4) --> ABCD BCDE CDEF DEFG
        it = iter(iterable)
        window = deque(islice(it, n-1), maxlen=n)
        for x in it:
            window.append(x)
            yield tuple(window)

class CipherTextScorer:
    def __init__(self, ngram_length):
        assert ngram_length >= 1
        if ngram_length == 1:
            print("You have selected an NGram length of one!")
            print("Make sure this is not an error")
        self.ngram_length = ngram_length
        self.ngram_loge_probabilities = {}
        self.base_loge_probability = 0
        self.ngram_count_dict = {}
        self.total_number_of_ngrams = 0

    def __ngram_file_validation(self, line):
        try:
            assert len(line.split(" ")) == 2
            ngram, count = line.split(" ")
            assert set(ngram) <= set(ascii_uppercase)
            assert len(ngram) == self.ngram_length
            assert int(count) >= 1 and int(float(count)) == int(count)
            return tuple(ngram), int(count)
        except:
            raise TypeError()

    def __calculate_loge_probabilities(self):
        assert len(self.ngram_count_dict) <= self.total_number_of_ngrams
        if len(self.ngram_count_dict) < 26:
            raise TypeError("More ngrams are needed (more than 26 at least)")
        for each_ngram in self.ngram_count_dict:
            ngram_count = self.ngram_count_dict[each_ngram]
            self.ngram_loge_probabilities[each_ngram] = log(ngram_count/self.total_number_of_ngrams)
        ngram_count = 0.01
        self.base_loge_probability = log(ngram_count/self.total_number_of_ngrams)
        del self.ngram_count_dict

    def load_ngram_file(self, fileName):
        with open(fileName, 'r') as file:
            for line in file:
                ngram, count = self.__ngram_file_validation(line)
                self.ngram_count_dict[ngram] = count
                self.total_number_of_ngrams += count
        self.__calculate_loge_probabilities()

    def calculate_score(self, iterable):
        #comment the line below to squeeze out last bits or performance - not significant in normal intensive use
        #assert set(iterable) <= set(ascii_uppercase)
        #if base_probability == None: base_probability = self.base_loge_probability
        base_probability = self.base_loge_probability
        score = 0
        for tuple in sliding_window(iterable, self.ngram_length):
            score += self.ngram_loge_probabilities[tuple] if tuple in self.ngram_loge_probabilities else base_probability
        return score
"""
scorer = CipherTextScorer(4)
scorer.load_ngram_file("quadgrams.txt")
if __name__ == '__main__':
  def main():
    a = ("YZYQ")
    b = ("ASERSHKNKBJHBHGRSDTNKBJHGTFDTFTGHHJKJ")
    for i in range(100):
        #shuffle(a)
        #shuffle(b)
        print(scorer.calculate_score(a, +989828199))
        print(scorer.calculate_score(b))
    #print("done")


  from timeit import timeit
  print(timeit(stmt=main, number=1000))
  #main()
"""
