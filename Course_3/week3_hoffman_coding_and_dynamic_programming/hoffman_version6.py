"""
In this programming problem and the next you'll code up the greedy algorithm from the lectures
on Huffman coding.
This and version 4 are the best versions: Using iteration insted of recursion, but more impotantly:
using HEAPS to speed up things. Compared to version3, this uses  tuples insted of lists (still faster)

Code-wise, this is the simplest of all the versions. But not remarkably fast, for some reason.
Krms 14/1/2018
"""

from heapq import*

class Tree:
    """
    Recursive definition for trees plus various tree methods.
    This is a modified version of poc_tree.
    """

    def __init__(self, children, value = None):
        """
        Create a tree whose root has specific value (a string)
        Children is a list of references to the roots of the subtrees.
        """

        if children == ():
            self._value = value

        self._children = children


    def __str__(self):
        """
        Generate a string representation of the leaces of the tree
        """

        return str(self._value)

    def get_value(self):
        """
        Getter for node's value
        """
        return self._value

    def children(self):
        """
        Generator to return children
        """
        for child in self._children:
            yield child

    def num_nodes(self):
        """
        Compute number of nodes in the tree
        """
        ans = 1
        for child in self._children:
            ans += child.num_nodes()
        return ans

    def num_leaves(self):
        """
        Count number of leaves in tree
        """
        if len(self._children) == 0:
            return 1

        ans = 0
        for child in self._children:
            ans += child.num_leaves()
        return ans

    def height(self):
        """
        Compute height of a tree rooted by self
        """
        height = 0
        for child in self._children:
            height = max(height, child.height() + 1)
        return height

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
        heappush(heap, (weight, Tree((), char_number)))
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
        merged_tree = Tree((tree_1, tree_2))
        heappush(char_list, (weight_1 + weight_2, merged_tree))

    tree_1 = heappop(char_list)[1]
    tree_2 = heappop(char_list)[1]

    return Tree((tree_1, tree_2))

alpha_tree = make_tree(ALPHABETH)

HOFFMANN_CODES = {}

def hoffmann_codes(tree, code_so_far):
    """
    This function takes a "Hoffmann tree" made out of some alphabeth and builds a dictionary with
    the Hoffmann_codes of the alphabeth
    """
    if tree._children == ():
        HOFFMANN_CODES[tree._value] = code_so_far
    else:
        hoffmann_codes(tree._children[0], code_so_far + "0")
        hoffmann_codes(tree._children[1], code_so_far + "1")

hoffmann_codes(alpha_tree, "")
print HOFFMANN_CODES[200]
print HOFFMANN_CODES[351]

def longest_code(code_dict):
    #lengths = [len(val) for val in code_dict.values()]
    #print min(lengths)
    #print max(lengths)
    sorted_codes = sorted(code_dict.items(), key = lambda x: len(x[1]))
    print "Shortest:", sorted_codes[0], len(sorted_codes[0][1])
    print "Longest:", sorted_codes[-1], len(sorted_codes[-1][1])

longest_code(HOFFMANN_CODES)
