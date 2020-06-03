import re


def word_count(s):
    words = dict()
    space = re.sub(r'[ \t\n\r\f\v]', ' ', s.lower())
    clean = [re.sub(r'[^\w\||\']', '', y.replace("|", ""))
             for y in space.split(" ")]
    for w in clean:
        if len(w) > 0:
            words[w] = 1 + words.get(w, 0)
    return words


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))
