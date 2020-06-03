# Your code here

import re
from os import path

# Read in all the words in one go
robin_text = path.join(path.dirname(path.abspath(__file__)), "robin.txt")
with open(robin_text) as f:
    words = f.read()

words_list = " ".join(words.split('\n')).split(" ")
word_count = dict()  # "hashtable"


def word_cleaner(word):
    space = re.sub(r'[ \t\n\r\f\v]', ' ', word.lower())  # whitespaces
    clean = [re.sub(r'[^\w]', '', y.replace("|", ""))
             for y in space.split(" ")]  # remove punct
    return "".join(clean)


longest_word = [0, ""]  # [length, word]

for w in words_list:
    # find longest word
    key = word_cleaner(w).strip()
    if len(key) > 0:
        word_count[key] = 1 + word_count.get(key, 0)
        last = longest_word[0]
        [nxt, wrd] = [len(key), key]
        if nxt > last:
            longest_word = [nxt, wrd]

word_space = longest_word[0] + 2  # width of the word column


def histogram(order="asc"):
    group_keys = sorted(list(set([word_count[i] for i in word_count.keys()]))) \
        if order not in ["d", "desc", "descending"] \
        else sorted(list(set([word_count[i] for i in word_count.keys()])), reverse=True)
    for key in group_keys:
        ab = sorted([item for item in word_count.keys()
                     if word_count[item] == key])
        for w in ab:
            margin = word_space - len(w)
            print(f"{w} : {' ' * margin}{'#' * word_count[w]}")


if __name__ == "__main__":
    # histogram()
    histogram(order="desc")
