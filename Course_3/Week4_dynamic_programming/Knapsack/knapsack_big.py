"""
This problem also asks you to solve a knapsack instance, but a much bigger one.
"""

import numpy as np
import sys
sys.setrecursionlimit(20000)

def load_data():
    """
    Reads data from file. Stores data in a list items, where items[i] = (value of item(i+1), weight of item(i+1))
    """
    fh = open('knapsack_big.txt')
    #fh = open('knapsack1.txt')
    data = fh.read()
    data_lines = data.split('\n')
    knapsack_size, num_items = data_lines[0].split()
    print "Read data for knapsack problem from file.\nThe size of the knapsack is {} and the total number of items is {}".format(knapsack_size, num_items)
    knapsack_size = int(knapsack_size)
    num_items = int(num_items)
    items = []
    for line in data_lines[1:-1]:
        value, weight = line.split()
        items.append((int(value),int(weight)))
    items = np.array(items)
    return items, knapsack_size, num_items


def opt(i, x, knapsack_dict):
    """
    Solves knapsack problem recursively - using memorization. Takes around 100 seconds for the BIG problem.
    The iterative approch does not work in this case, as the matrix gets way to big.
    """
    potential_answer = knapsack_dict.get((i,x), None)
    if potential_answer is not None:
        return potential_answer
    #if (i, x) in knapsack_dict:
    #    return knapsack_dict[(i,x)]

    if i == 0 or x == 0:
        knapsack_dict[(i,x)] = 0
        return 0

    val_i, weight_i = items[i - 1]

    if weight_i <= x:
        answer = max(opt(i - 1, x, knapsack_dict), opt(i - 1, x - weight_i, knapsack_dict) + val_i)
    else:
        answer = opt(i - 1, x, knapsack_dict)

    knapsack_dict[(i,x)] = answer
    return answer

items, knapsack_size, num_items = load_data()
print "Optimal value for big knapsack problem:", opt(num_items, knapsack_size, {})

#print opt(num_items, knapsack_size, {}) == 2493893

def test_cases():
    global items

    test_data1 = [(3,4)], 6, 1
    test_data2 = [], 6, 0
    test_data3 = [(3,4), (2,3)], 6, 2
    test_data35 = [(3,4), (2,3)], 7, 2
    test_data4 = [(3,4), (2,3), (4,2)], 6, 3
    test_data5 = [(3,4), (2,3), (4,2), (4,3)], 6, 4

    items, knapsack_size, num_items = test_data2
    print opt(num_items, knapsack_size, {}) == 0

    items, knapsack_size, num_items = test_data1
    print opt(num_items, knapsack_size, {}) == 3

    items, knapsack_size, num_items = test_data3
    print opt(num_items, knapsack_size, {}) == 3

    items, knapsack_size, num_items = test_data35
    print opt(num_items, knapsack_size, {}) == 5

    items, knapsack_size, num_items = test_data4
    print opt(num_items, knapsack_size, {}) == 7

    items, knapsack_size, num_items = test_data5
    print opt(num_items, knapsack_size, {}) == 8

test_cases()
