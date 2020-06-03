import math

# https://mail.python.org/pipermail/python-list/2000-March/048085.html
expensive_answers = dict()


def expensive_seq(x, y, z):
    key = (x, y, z)
    ans = expensive_answers.get(key, None)
    if ans is None:
        if x <= 0:
            ans = y + z
        else:
            ans = expensive_seq(x-1, y+1, z) + \
                expensive_seq(x-2, y+2, z*2) + \
                expensive_seq(x-3, y+3, z*3)
        expensive_answers[key] = ans
    return ans


if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
