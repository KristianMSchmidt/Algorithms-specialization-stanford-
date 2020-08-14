"""
Super smart solution - I wish it was my own.
Uses library bisect to make binary fast search in ordered lists.

NB: I think the python library "sorted collection" is even better than bisect for working
with sorted lists.
"""
from bisect import *

def make_list_from_data():
    fh = open('million_integers.txt')
    data = fh.read()
    data_lines = data.split('\n')
    data_lines = data_lines[:-1]
    return [int(num) for num in data_lines]

integers = make_list_from_data()


def find_ge(a, x):
    'Find leftmost index with value greater than or equal to x'
    i = bisect_left(a, x)
    if i != len(a):
        return i
    return None

def find_le(a, x):
    'Find rightmost index with value less than or equal to x'
    i = bisect_right(a, x)
    if i:
        return i-1
    return None

def best_solution(number):
    """
    Uses the fact that for given number x, the only interesting y values are in this very narrow interval:
    - 10000 =< x + y <= 100000
    - 10000 - x =< y <= 10000 - x
    Only takes 4 seconds!
    This solution has running time: n*O(log(n))
    """
    count = 0
    integers.sort()
    hit = set()

    for num1 in integers:
        lower = find_ge(integers, - 10000 - num1)
        upper = find_le(integers, 10000 - num1)
        if lower != None and upper != None:
            for num2 in integers[lower: upper + 1]:
                if num1 != num2:
                    hit.add(num1 + num2)
    return len(hit)

print best_solution(10000)
