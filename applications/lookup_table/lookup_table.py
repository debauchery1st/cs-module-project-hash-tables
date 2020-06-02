# Your code here
from hashtable import HashTable
import math
import random


def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653
    return v


mem_hash = HashTable(36)


def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    key = f"o_{x}_{y}"
    result = mem_hash.get(key)
    if result is not None:
        v = result
    else:
        v = math.factorial(math.pow(x, y))
        v //= (x+y)
        v %= 982451653
        mem_hash.put(key, v)
    return v


# Do not modify below this line!
for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
