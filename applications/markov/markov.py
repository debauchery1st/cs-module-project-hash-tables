import re
import random
from os import path
# Read in all the words in one go
textfile = path.join(path.dirname(path.abspath(__file__)), "input.txt")
with open(textfile) as f:
    words = f.read()

# analyze which words can follow other words
followers = {}
l = " ".join(words.split("\n")).split(" ")
for i, wrd in enumerate(l):
    distance = (len(l) - i)
    have = followers.get(wrd, [])
    if wrd not in have and distance > 1:
        have.append(l[i+1])
        followers[wrd] = have

# construct random sentences


def start_word(s):
    """
    sentence starter?
    """
    key = re.sub(r'[^\w]', '', s)
    if len(key) == 0:
        return False
    return (len(key) > 1 and
            key[0] == '"' and
            key[1].upper() == key[1]) \
        or key[0].upper() == key[0]


def stop_word(s):
    """
    sentence stopper ?
    """
    if len(s) == 0:
        return False
    if s[-1] == ',':
        return False
    punc = re.sub(r'[\w]', '', s[-1])
    if not punc:
        return False
    return s[-1] in punc


starters = list(filter(start_word, followers.keys()))
stoppers = list(filter(stop_word, followers.keys()))


def choose_starter():
    """
    choose a random sentence starter
    """
    return starters[random.randrange(len(starters))]


def choose_stopper():
    """
    choose a random sentence stopper
    """
    return stoppers[random.randrange(len(stoppers))]


def choose_follower(s, exclude=None):
    """
    choose randomly, from followers
    """
    try:
        choices = list(filter(lambda flr: flr != exclude, followers[s]))
    except KeyError:
        choices = l  # random choice
    if len(choices) == 0:
        # stop the sentence if we have no followers.
        return choose_stopper()
    # randomly choose from followers
    return choices[random.randrange(len(choices))]


def write_sentence(n, max_words=24):
    """
    Construct 'n'-many sentences; Each limited to 'max_words' number of words.
    """
    paragraph = list()  # holds constructed sentences
    for _ in range(n):
        sentence = list()  # holds sentence
        sentence.append(choose_starter())  # start of sentence
        last = sentence[-1]  # last word of sentence
        count = 0  # how many words are in this sentence
        while not stop_word(last):
            count += 1  # increase word count
            if count > max_words:
                # end the sentence
                last = choose_stopper()
            else:
                # continue the sentence
                last = choose_follower(last, exclude=last)
            if last[-1] == '"':
                # quotes will be automatically closed after loop
                last = last[:-1]  # remove ending quotation mark
            sentence.append(last)
        result = " ".join(sentence)  # recombine into string
        if result.count('"') % 2 != 0:
            # if quotes are unbalanced,
            result += '"'  # add quotation mark
        paragraph.append(result)  # add sentence to paragraph
    return "\n".join(paragraph)


if __name__ == "__main__":
    print(write_sentence(5))
