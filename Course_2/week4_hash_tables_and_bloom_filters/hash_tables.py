"""
Solution to week 4's programming exercise.
Morale: It's fast to look up in hashtables
"""

def make_list_from_data():
    fh = open('million_integers.txt')
    data = fh.read()
    data_lines = data.split('\n')
    data_lines = data_lines[:-1]
    data_list = [int(num) for num in data_lines]
    data_dict = {}
    print "Constructed list with {} integers from text file".format(len(data_lines))
    for num in data_list:
        data_dict[num] = None
    print "Constructed dictionary from list"
    print "There are {} different integers in the list".format(len(data_dict))
    data_set = set()
    for num in data_list:
        data_set.add(num)

    return data_list, data_dict, data_set

integers, integers_hash, integers_set = make_list_from_data()

##Naive attempt.Does not work at all. Way to slow!!
def naive_solution(number):
    """
    This is not even close to working. 20000*1000000**2
    Even checking only in the range (-1, 1) takes a very loong time.
    """
    answer = 0
    for target_value in range(-number, number + 1):
        for int1 in integers:
            sub_target = target_value - int1
            if sub_target != int1:
                if sub_target in integers:
                    answer += 1
    return answer
#naive_solution(1)


def binarySearch(alist, item):
    """
    Binary search in sorted list
    I found this helper function on the net.
    Could probably also have used the "bisect module" from the official package.
    """
    first = 0
    last = len(alist)-1
    found = False

    while first<=last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    return found

def better_solution(number):
    """
    Still suboptimal solution
    This takes approximataly 10 secs per target value, so for the full range (-10000, 10000) it would
    take 200.000 secs ... aroud an 55 hours!
    """
    integers.sort()
    answer = 0
    for target_value in range(-number, number + 1):
        print "Checking target_value:", target_value
        for int1 in integers:
            sub_target = target_value - int1
            if sub_target != int1:
                if binarySearch(integers, sub_target):
                    answer += 1
                    print "Target value {} got hit".format(target_value)
                    break
    print answer
#better_solution(10)


def best_solution(number):
    """
    This is the suggested solution.
    The point of this solution (compared to the one above)
    is that it is faster to look up in a dictionary than to look
    for a value in an (even sorted) list.
    This takes around 16 secs for 20 values, so it will take around 16000 sec for all 20000 values.
    Result is 427. Takes 8960 sec = 2,5 timer.
    """
    count = 0
    for target_value in range(-number, number + 1):
        if target_value % 100 == 0:
            print "Checking target_value:", target_value
            print "Count: ", count
        for int1 in integers_set:
            sub_target = target_value - int1
            if sub_target != int1:
                #if sub_target in integers_hash:
                if sub_target in integers_set:
                    count += 1
                    #print "Target value {} got hit".format(target_value)
                    break
    print "Total count:", count

best_solution(10000)
