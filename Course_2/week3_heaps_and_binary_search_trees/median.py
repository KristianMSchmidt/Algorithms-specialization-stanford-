"""
Median Maintanance.
Using heaps. (Running time should be 0(log(i)) at each step i)
Using binary search trees: See binary tree file.
"""
from heapq import*

def median_maintanance2(some_list):
    """
    Returns medians of incomming numbers as they arrive.
    Argument kan be list or tuple or generator
    I guess this could be optimized a bit by going through some details and thinking about special cases. But
    Also, heapq supports some fast solutions when you both want to push and pop.
    """
    h_low = []
    h_high = []

    answer = []

    if len(some_list) < 2:
        return some_list

    else:
        h_low = [-1 * min(some_list[0], some_list[1])]
        h_high = [max(some_list[0], some_list[1])]
        answer = [some_list[0], -1*h_low[0]]

    for num in some_list[2:]:
        low_max = -1* h_low[0]
        high_min = h_high[0]

        if num < low_max:
            heappush(h_low, -1*num)
        else:
            heappush(h_high, num)

        if len(h_low) == len(h_high):
            answer.append(-1*h_low[0])

        elif len(h_low) < len(h_high):
            if len(h_low) == len(h_high) - 1:
                answer.append(h_high[0])
            else:
                median = heappop(h_high)
                heappush(h_low,-1*median)
                answer.append(median)

        else: #len(h_high) < len(h_low)
            if len(h_high) == len(h_low) - 1:
                answer.append(-1*h_low[0])
            else:
                to_move = -1*heappop(h_low)
                heappush(h_high, to_move)
                answer.append(-1*h_low[0])
    return answer



def median_maintanance(some_tuple):
    """
    Returns medians of incomming numbers as they arrive.
    Argument kan be list or tuple or generator
    I guess this could be optimized a bit by going through some details and thinking about special cases. But
    Also, heapq supports some fast solutions when you both want to push and pop.
    """
    h_low = []
    h_high = []

    answer = []

    for num in some_tuple:
        #Taking care of first two loops
        if h_low == []:
            h_low = [-1*num]  #minus is to make heapq-queue a "fake" max queue
            answer.append(num)
        elif h_high == []:
            if num < -1*h_low[0]:
                h_high = [-1*h_low[0]]
                h_low = [-1*num]
                answer.append(num)
            else:
                h_high = [num]
                answer.append(-1*h_low[0])
        #Done with first two loops
        else:
            low_max = -1* h_low[0]
            high_min = h_high[0]

            if num < low_max:
                heappush(h_low, -1*num)
            else:
                heappush(h_high, num)

            if len(h_low) == len(h_high):
                answer.append(-1*h_low[0])

            elif len(h_low) < len(h_high):
                if len(h_low) == len(h_high) - 1:
                    answer.append(h_high[0])
                else:
                    median = heappop(h_high)
                    heappush(h_low,-1*median)
                    answer.append(median)

            else: #len(h_high) < len(h_low)
                if len(h_high) == len(h_low) - 1:
                    answer.append(-1*h_low[0])
                else:
                    to_move = -1*heappop(h_low)
                    heappush(h_high, to_move)
                    answer.append(-1*h_low[0])
    return answer

#Some test cases
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
#
# print median_maintanance2(numbers1) == list(medians1)
# print median_maintanance2(numbers2) == list(medians2)
# print median_maintanance2(numbers3) == list(medians3)
#

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

# test_case1 = [1, 666, 10,667,100,2,3]
# test_case2 = [6331,2793,1640,9290,225,625,6195,2303,5685,1354]

# print assignment(median_maintanance(test_case1)) == 142
# print assignment(median_maintanance(test_case2)) == 9335
# print assignment(median_maintanance(make_list_from_data())) == 1213

# print assignment(median_maintanance2(test_case1)) == 142
# print assignment(median_maintanance2(test_case2)) == 9335
print assignment(median_maintanance2(make_list_from_data())) == 1213
