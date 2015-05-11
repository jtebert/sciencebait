import random
import os


def import_words(str_file):
    str_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), str_file)
    all_words = open(str_file).readlines()
    all_words = [x.replace('\n', '') for x in all_words]
    all_words = [x.split(', ') for x in all_words]
    # Print out any errors?
    """
    for i in range(len(all_words)):
        if len(all_words[i]) == 1:
            print all_words[i]
    """
    x = zip(*all_words)
    return x


def pick_plural_or_general(paired, one):
    n = random.randint(0, 1)
    if n == 0:
        return paired.pick_plural()
    else:
        return one.pick()


def format_num(n):
    return "{:,}".format(n)


def get_pronoun(s):
    if s == 'm':
        return 'he'
    elif s == 'f':
        return 'she'
    elif s == 'p':
        return 'they'
    else:
        return 'it'


def get_pronoun_acc(s):
    if s == 'm':
        return 'him'
    elif s == 'f':
        return 'her'
    elif s == 'p':
        return 'them'
    else:
        return 'it'


class PairedType:
    def __init__(self, str_file):
        all_words = import_words(str_file)
        self.single = all_words[0]
        self.num_single = len(self.single) - 1
        self.plural = all_words[1]
        self.num_plural = len(self.plural) - 1

    def pick_single(self):
        i = random.randint(0, self.num_single)
        #print i, len(self.single)
        return self.single[i]

    def pick_plural(self):
        i = random.randint(0, self.num_plural)
        #print i, len(self.plural)
        return self.plural[i]


class GenderedType:
    def __init__(self, str_file):
        all_words = import_words(str_file)
        self.words = zip(all_words[0], all_words[1])
        self.num_words = len(self.words) - 1

    def pick(self):
        i = random.randint(0, self.num_words)
        # print i, len(self.single)
        return self.words[i]


class OneType:
    def __init__(self, str_file):
        all_words = import_words(str_file)
        self.words = all_words[0]
        self.num_words = len(self.words) - 1

    def pick(self):
        i = random.randint(0, self.num_words)
        #print i, len(self.words)
        return self.words[i]


class NumberType:
    def __init__(self):
        self.numbers = range(2, 30)
        self.numbers.extend([1325, 666, 27512, 99, 101, 573])
        self.num_numbers = len(self.numbers) - 1

    def pick(self):
        i = random.randint(0, self.num_numbers)
        #print i, len(self.numbers)
        return self.numbers[i]


def a_an(string):
    if string[0].lower() in ['a', 'e', 'i', 'o', 'u']:
        return 'an'
    else:
        return 'a'