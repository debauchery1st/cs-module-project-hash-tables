def no_dups(s):
    dupeCheck = dict()
    answer = []
    for wrd in s.split(" "):
        if dupeCheck.get(wrd, 0) == 0:
            dupeCheck[wrd] = 1
            answer.append(wrd)
    return " ".join(answer)


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
