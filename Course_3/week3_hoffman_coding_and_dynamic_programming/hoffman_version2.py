"""
In this programming problem and the next you'll code up the greedy algorithm from the lectures
on Huffman coding.
Krms 12/1/2018
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

        if children == []:
            self._value = value
        else:
            self._value = children[0]._value + children[1]._value
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
    Read data from file.
    Return a list of the form
     [(2, [6]), (3, [5]), (4, [9]),...]
    where (2, [6]) means that character number 6 has value 2.
    """
    fh = open('hoffman_data.txt')
    data = fh.read()
    data_lines = data.split('\n')
    num_characters = data_lines[0]
    print "Numbers of characters in alpabeth: {}".format(num_characters)
    print "Each character has a weight (= importance/high usage)"
    alphabeth = []
    char_number = 1
    heap = []
    for line in data_lines[1: -1]:
        heappush(heap, (int(line), [char_number]))
        alphabeth.append((int(line), [char_number]))
        char_number += 1
    alphabeth.sort()
    return alphabeth, heap
ALPHABETH =  load_data()[0]
ALPH = load_data()[1]
#print heappop(ALPH)

def make_tree(char_list):
    """
    Takes a weighted character_list (aka an alphabeth) sorted by weight and makes a tree according to Hoffmanns algorithm
    """
    tree_dict = {}

    tree_dict = {}
    for char in char_list:
        character_number = char[1]
        tree_dict[str(character_number)] = Tree([], character_number)

    while len(char_list) > 2:
        weight_1, char_number_1 = char_list[0]
        weight_2, char_number_2 = char_list[1]
        #print "joining", char_number_1, char_number_2
        char_list = char_list[2:]
        char_list.append((weight_1 + weight_2, char_number_1 + char_number_2))

        tree1 = tree_dict[str(char_number_1)]
        tree2 = tree_dict[str(char_number_2)]
        tree_dict[str(char_number_1 + char_number_2)] = Tree([tree1, tree2])
        #trees.pop(str(x1))
        #trees.pop(str(x2))
        #print ""
        #print trees
        ##The below is inefficient...I should use that the list is nearly sorted
        char_list.sort()
        #return make_tree(char_list)
        #return make_tree(char_list_list[2:], )

    #    print "len 2"
        #print "only two left"
        #print "char_list", char_list
    #print "joining", char_list[0][1], char_list[1][1]
    char_number_1 = char_list[0][1]
    char_number_2 = char_list[1][1]

    return Tree([tree_dict[str(char_number_1)], tree_dict[str(char_number_2)]])


#print ALPHABETH
alpha_tree = make_tree(ALPHABETH)
#print "fin tree", alpha_tree

HOFFMANN_CODES = {}

def hoffmann_codes(tree, code_so_far):
    """
    This function takes a "Hoffmann tree" made out of some alphabeth and builds a dictionary with
    the Hoffmann_codes of the alphabeth
    """
    if tree._children == []:
        HOFFMANN_CODES[tree._value[0]] = code_so_far
    else:
        hoffmann_codes(tree._children[0], code_so_far + "0")
        hoffmann_codes(tree._children[1], code_so_far + "1")

hoffmann_codes(alpha_tree, "")
#print HOFFMANN_CODES


def longest_code(code_dict):
    #sorted_codes = sorted(code_dict.values(), key = lambda x: len(x))
    sorted_codes = sorted(code_dict.items(), key = lambda x: len(x[1]))
    print "Shortest:", sorted_codes[0], len(sorted_codes[0][1])
    print "Longest:", sorted_codes[-1], len(sorted_codes[-1][1])

longest_code(HOFFMANN_CODES)
