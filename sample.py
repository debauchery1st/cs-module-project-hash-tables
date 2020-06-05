#! /bin/env python3
from functools import reduce

numbers_memo = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10,
    "eleven": 11,
    "twelve": 12,
    "thirteen": 13,
    "fourteen": 14,
    "fifteen": 15,
    "sixteen": 16,
    "seventeen": 17,
    "eighteen": 18,
    "nineteen": 19,
    "twenty": 20,
    "thirty": 30,
    "forty": 40,
    "fifty": 50,
    "sixty": 60,
    "seventy": 70,
    "eighty": 80,
    "ninety": 90,
    "hundred": 100,
    "thousand": 1000,
}

def intFromWord(num):
    test = list(map(lambda n: numbers_memo[n], num.split(" ")))
    try:
        if test[1] in [100, 1000, 100000]:
            mult = test.pop(0)
            test[0] = mult * test[0]
    except IndexError:
        pass
    return reduce(lambda a, b: b+a, test)


def divisibleByThree(wrds):
    return list(filter(lambda w: intFromWord(w) % 3 == 0, wrds))


if __name__ == "__main__":
    numbers = [
        "five",
        "twenty six",
        "nine hundred ninety nine",
        "twelve",
        "eighteen",
        "one hundred one",
        "fifty two",
        "forty one",
        "seventy seven",
        "six",
        "twelve",
        "four",
        "sixteen"
    ]
    for answer in divisibleByThree(numbers):
        print(answer)
