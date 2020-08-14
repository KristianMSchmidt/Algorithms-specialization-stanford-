"""
In this programming problem and the next you'll code up the knapsack algorithm from lecture.

The file describes a knapsack instance, and it has the following format:
[knapsack_size][number_of_items]
[value_1] [weight_1]
[value_2] [weight_2]

For example, the third line of the file is "50074 659", indicating that the second item has value 50074 and size 659, respectively.

You can assume that all numbers are positive. You should assume that item weights and the knapsack capacity are integers.

In the box below, type in the value of the optimal solution.

The below solutions could without doubt be made faster using numpy.
"""

def load_data():
    """
    Reads data from file. Stores data in a list items, where items[i] = (value of item(i+1), weight of item(i+1))
    """
    fh = open('knapsack1.txt')
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
    return items, knapsack_size, num_items

test_data1 = [(3,4)], 6, 1
test_data2 = [], 6, 0
test_data3 = [(3,4), (2,3)], 6, 2
test_data4 = [(3,4), (2,3), (4,2)], 6, 3
test_data5 = [(3,4), (2,3), (4,2), (4,3)], 6, 4


def opt_knapsack():
    """
    Solves knapsack problem iteratively without storing the whole matrix - only the last row. This is faster.
    """
    items, knapsack_size, num_items = load_data()
    next_row = [0 for dummy in range(knapsack_size + 1)]

    for i in range(1, num_items + 1):
        previous_row = list(next_row)
        val_i, weight_i = items[i - 1]
        for x in range(knapsack_size + 1):
            if weight_i <= x:
                next_row[x] = max(previous_row[x], previous_row[x - weight_i] + val_i)
            else:
                next_row[x] = previous_row[x]

    print "The optimal value for the knapsack problem is {}".format(next_row[-1])
    return next_row[-1]

print opt_knapsack() == 2493893

def opt_knapsack():
    """
    Solves knapsack problem iteratively by building a whole matrix.
    """
    items, knapsack_size, num_items = load_data()
    #items, knapsack_size, num_items = test_data3 # = 3
    #items, knapsack_size, num_items = test_data5 # = 8

    A = [[0 for dummy in range(knapsack_size + 1)] for dummy in range(num_items + 1)]
    for i in range(1, num_items + 1):
        val_i, weight_i = items[i - 1]
        for x in range(knapsack_size + 1):
            if weight_i <= x:
                A[i][x] = max(A[i - 1][x], A[i - 1][x - weight_i] + val_i)
            else:
                A[i][x] = A[i - 1][x]
    print "The optimal value for the knapsack problem is {}".format(A[-1][-1])
    return A[-1][-1]
#print opt_knapsack() == 2493893


def opt_knapsack():
    """
    Same as above - just with matrix implemted as dictionary of dictionaries. This is slower.
    """
    items, knapsack_size, num_items = load_data()
    #items, knapsack_size, num_items = test_data3 # = 3
    #items, knapsack_size, num_items = test_data5 # = 8

    A = {}
    A[0] = {}
    for x in range(knapsack_size + 1):
        A[0][x] = 0
    for i in range(1, num_items + 1):
        A[i] = {}
        val_i, weight_i = items[i - 1]
        for x in range(knapsack_size + 1):
            if weight_i <= x:
                A[i][x] = max(A[i - 1][x], A[i - 1][x - weight_i] + val_i)
            else:
                A[i][x] = A[i - 1][x]
    print "The optimal value for the knapsack problem is {}".format(A[num_items][knapsack_size])
#opt_knapsack()
