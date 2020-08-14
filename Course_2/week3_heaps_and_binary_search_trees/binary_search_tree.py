"""
I found a simpler version of the below implementation of binary search tree randomly on github.
I've augmented with max, min, print and vals_in_order methods.
I've also change the Node class so that it now contains information about size of it's branch and a method
to calculate k'th order statistics of tree and the median value

Krms 5/1/2018
"""


class Node:
    def __init__(self, val):
        self._val = val
        self._left_child = None
        self._right_child = None
        self._size = 1

    def __str__(self):
        answer = [self._val]
        if self._left_child is None:
            answer.append([])
        else:
            answer.append([self._left_child._val])

        if self._right_child is None:
            answer.append([])
        else:
            answer.append([self._right_child._val])

        return str(answer)

    def get_value(self):
        return self._val

    def set_value(self, val):
        self._val = val

    def has_left_child(self):
        if self._left_child is None:
            return False
        else:
            return True

    def has_right_child(self):
        if self._right_child is None:
            return False
        else:
            return True

    def get_right_child(self):
        return self._right_child

    def get_left_child(self):
        return self._left_child

    def get_right_child(self):
        return self._right_child

    def get_children(self):
        children = []
        if(self._left_child != None):
            children.append(self._left_child)
        if(self._right_child != None):
            children.append(self._right_child)
        return children


class BST:
    def __init__(self):
        self._root = None

    def __str__(self):
        if self._root is None:
            return "Empty tree"
        return self._str(self._root)

    def _str(self, current_node):

        if current_node.has_left_child():
            left_answer = self._str(current_node.get_left_child())
        else:
            left_answer = ""

        if current_node.has_right_child():
            right_answer = self._str(current_node.get_right_child())
        else:
            right_answer = ""

        if left_answer == "" and right_answer == "":
            return str(current_node)
        elif left_answer == "":
            return str(current_node) + ", " + right_answer
        elif right_answer == "":
            return str(current_node) + ", " + left_answer
        else:
            return str(current_node) + ", " + left_answer + ", " + right_answer

    def size(self):
        return self._root._size

    def _set_root(self, val):
        self._root = Node(val)

    def get_root(self):
        return self._root

    def insert(self, val):
        if(self._root is None):
            self._set_root(val)
        else:
            self._insert_node(self._root, val)

    def _insert_node(self, current_node, val):
        current_node._size += 1

        if(val <= current_node._val):
            if(current_node._left_child):
                self._insert_node(current_node._left_child, val)
            else:
                current_node._left_child = Node(val)
        elif(val > current_node._val):
            if(current_node._right_child):
                self._insert_node(current_node._right_child, val)
            else:
                current_node._right_child = Node(val)

    def find(self, val):
        return self._find(self._root, val)

    def _find(self, current_node, val):
        if(current_node is None):
            return False
        elif(val == current_node.get_value()):
            return True
        elif(val < current_node.get_value()):
            return self._find(current_node._left_child, val)
        else:
            return self._find(current_node._right_child, val)

    def get_node(self, val):
        return self._get_node(self._root, val)

    def _get_node(self, current_node, val):
        assert current_node != None

        if(val == current_node.get_value()):
            return current_node
        elif(val < current_node.get_value()):
            return self._get_node(current_node._left_child, val)
        else:
            return self._get_node(current_node._right_child, val)


    def get_min(self):
        return self._get_min(self._root)

    def _get_min(self, current_node):
       if not current_node.has_left_child():
           return current_node.get_value()
       else:
           return self._get_min(current_node.get_left_child())

    def get_max(self):
        return self._get_max(self._root)

    def _get_max(self, current_node):
       if not current_node.has_right_child():
           return current_node.get_value()
       else:
           return self._get_max(current_node.get_right_child())

    def vals_in_order(self):
        """
        Returns all values in tree in increasing order
        """
        if self._root is None:
            return ""
        else:
            return self._vals_in_order(self._root)

    def _vals_in_order(self, current_node):
        answer = []
        if current_node.has_left_child():
            left_answer = self._vals_in_order(current_node.get_left_child())
        else:
            left_answer = []
        if current_node.has_right_child():
            right_answer = self._vals_in_order(current_node.get_right_child())
        else:
            right_answer = []
        return left_answer + [current_node.get_value()] + right_answer

    def k_order_stats(self, order):
        """
        Returns k'th order statistics of tree - that is, the kth smallest value of tree
        I have not testet this seriously
        """
        if self._root is None:
            print "Empty tree"
        else:
            return self._k_order_stats(order, self._root)

    def _k_order_stats(self, order, current_node):
        if current_node.has_left_child():
            left_size = current_node.get_left_child()._size
        else:
            left_size = 0

        if left_size == order - 1:
            return current_node.get_value()
        elif left_size >= order:
            return self._k_order_stats(order, current_node.get_left_child())
        else:
            return self._k_order_stats(order - left_size - 1, current_node.get_right_child())

    def median(self, tree_size = None):
        assert self._root != None
        if tree_size is None:
            tree_size = self._root._size
        if tree_size % 2:
            order = (tree_size + 1)/2
        else:
            order = tree_size/2
        return self._k_order_stats(order, self._root)

def median_maintanance(some_list):
    answer = []
    tree = BST()

    for num in some_list:
        tree.insert(num)
        answer.append(tree.median())

    return answer

# numbers1 =   (3, 1,  2 , 0,  5, 10, 11, 12, -1, -1 )
# medians1 = (3, 1,  2,  1, 2,  2,  3,   3,  3,  2)
#
# numbers2 =  (8,7,6,5,4,3,2,1)
# medians2   =(8, 7, 7, 6, 6, 5, 5, 4)
#
# numbers3 = (1,2,3,4,5,6,7,8)
# medians3 = (1,1,2,2,3,3,4,4)
#
# print median_maintanance(numbers1) == list(medians1)
# print median_maintanance(numbers2) == list(medians2)
# print median_maintanance(numbers3) == list(medians3)

def make_list_from_data():
    """
    Actually this returns a generator, not a list. Just for fun.
    """
    fh = open('data.txt')
    data = fh.read()
    print "Read data from file"
    data_lines = data.split('\n')
    data_lines = data_lines[:-1]
    #data_lines = (int(num) for num in data_lines)
    data_lines = [int(num) for num in data_lines]

    return data_lines

def assignment(my_list):
    """
    Takes a list, and return the sum modulo 1000
    """
    return sum(my_list) % 10000

#test_case1 = [1, 666, 10,667,100,2,3]
#test_case2 = [6331,2793,1640,9290,225,625,6195,2303,5685,1354]

#print assignment(median_maintanance(test_case1)) == 142
#print assignment(median_maintanance(test_case2)) == 9335
print assignment(median_maintanance(make_list_from_data())) == 1213
