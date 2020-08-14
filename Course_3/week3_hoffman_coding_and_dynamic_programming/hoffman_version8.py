
print 1000* (0.32*2 + 0.25*2 + 0.2*2 + (0.18 + 0.05)*3)
"""
In this programming problem and the next you'll code up the greedy algorithm from the lectures
on Huffman coding.
This and version 4 are the best versions: Using iteration insted of recursion, but more impotantly:
using HEAPS to speed up things. Compared to version3, this uses  tuples insted of lists (still faster)

Code-wise, this is the simplest of all the versions. Does not even use tree class - just represents
trees as nested tuples (left_child, right_child) or (weight, leaf_node).

I also suppose that this version is the fastest (it seems very fast).
Krms 14/1/2018
"""

from heapq import heappush, heappop


def load_data():
    """
    Read data from file and make heap.
    """
    fh = open('hoffman_data.txt')
    data = fh.read()
    data_lines = data.split('\n')
    num_characters = data_lines[0]
    print "Numbers of characters in alpabeth: {}".format(num_characters)
    print "Each character has a weight (= importance/high usage)"
    char_number = 1
    heap = []
    for line in data_lines[1: -1]:
        weight = int(line)
        heappush(heap, (weight, char_number))
        char_number += 1
    return heap

ALPHABETH =  load_data()

def make_tree(char_list):
    """
    Takes a weighted character_list (aka an alphabeth) sorted by weight and makes a tree according to Hoffmanns algorithm
    """

    while len(char_list) > 2:
        weight_1, tree_1 = heappop(char_list)
        weight_2, tree_2 = heappop(char_list)
        merged_tree = (tree_1, tree_2)
        heappush(char_list, (weight_1 + weight_2, merged_tree))

    tree_1 = heappop(char_list)[1]
    tree_2 = heappop(char_list)[1]

    return (tree_1, tree_2)

alpha_tree = make_tree(ALPHABETH)

HOFFMANN_CODES = {}

def hoffmann_codes(tree, code_so_far):
    """
    This function takes a "Hoffmann tree" made out of some alphabeth and builds a dictionary with
    the Hoffmann_codes of the alphabeth
    """
    if type(tree) == int:
        HOFFMANN_CODES[tree] = code_so_far
    else:
        tree_1, tree_2 = tree
        hoffmann_codes(tree_1, code_so_far + "0")
        hoffmann_codes(tree_2, code_so_far + "1")

hoffmann_codes(alpha_tree, "")
#print HOFFMANN_CODES[200]
#print HOFFMANN_CODES[351]

def longest_code(code_dict):
    #lengths = [len(val) for val in code_dict.values()]
    #print min(lengths)
    #print max(lengths)
    sorted_codes = sorted(code_dict.items(), key = lambda x: len(x[1]))
    print "Shortest code {} has length {}".format(sorted_codes[0], len(sorted_codes[0][1]))
    print "Longest code {} has length {}".format(sorted_codes[-1], len(sorted_codes[-1][1]))

longest_code(HOFFMANN_CODES)
