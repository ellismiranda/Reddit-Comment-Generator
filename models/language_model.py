from collections import defaultdict
import nltk
import random
import bisect

START = '<S>'
STOP = '</S>'


class LanguageModel():

    def __init__(self):
        self.accu = defaultdict(list)
        self.unigrams = defaultdict(float)
        self.bigrams = defaultdict(float)

    def train(self, sentences):
        for sentence in sentences:
            tokens = nltk.tokenize.word_tokenize(sentence)
            prev = START
            self.unigrams[prev] += 1
            for word in tokens:
                self.unigrams[word] += 1
                self.bigrams[(prev, word)] += 1
                prev = word
            self.unigrams[STOP] += 1
            self.bigrams[(prev, STOP)] += 1

        for bigram in self.bigrams:
            self.accu[bigram[0]].append(self.bigrams[bigram]
                                            if len(self.accu[bigram[0]]) == 0
                                            else self.accu[bigram[0]][-1] + self.bigrams[bigram])
            self.bigrams[bigram] = self.bigrams[bigram] / self.unigrams[bigram[0]]

    def get_vocabulary(self, context):
        if len(context) == 0:
            ends = [second for first, second in self.bigrams if first == START]
        else:
            ends = [second for first, second in self.bigrams if first == context[-1]]
        return ends if len(ends) != 0 else self.unigrams.keys()

    def generate_word(self, context):
        ends = self.get_vocabulary(context)
        index = bisect.bisect_left(self.accu[context[-1]], random.randint(0, self.accu[context[-1]][-1]))
        return ends[index]

    def generate_sentence(self):
        sentence = [START]
        curr = None
        while curr != STOP:
            curr = self.generate_word(sentence)
            sentence.append(curr)
        return sentence
