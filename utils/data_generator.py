import numpy as np
import math
import random

def decode(i):
    k = math.floor((1+math.sqrt(1+8*i))/2)
    return k,i-k*(k-1)//2

def rand_pair(n):
    return decode(random.randrange(n*(n-1)//2))

def rand_pairs(n,m):
    return [decode(i) for i in random.sample(range(n*(n-1)//2),m)]

def generate_sum(min_: int, max_: int, amount: int, file_name: str):
    pairs = rand_pairs(max_-min_, amount)
    f = open(file_name, "a")
    for pair in pairs:
        first = pair[0] + min_
        second = pair[1] + min_
        f.write(str(first) + " " + str(second)  + " ; " + str(first+second) + "\n")
    f.close()

def generate_subtraction(min_: int, max_: int, amount: int, file_name: str):
    pairs = rand_pairs(max_-min_, amount)
    f = open(file_name, "a")
    for pair in pairs:
        first = pair[0] + min_
        second = pair[1] + min_
        f.write(str(first) + " " + str(second)  + " ; " + str(first-second) + "\n")
    f.close()

def generate_mult(min_: int, max_: int, amount: int, file_name: str):
    pairs = rand_pairs(max_-min_, amount)
    f = open(file_name, "a")
    for pair in pairs:
        first = pair[0] + min_
        second = pair[1] + min_
        f.write(str(first) + " " + str(second)  + " ; " + str(first*second) + "\n")
    f.close()

if __name__ == "__main__":
    generate_mult(-99, 99, 100, "example_1_2_E.txt")