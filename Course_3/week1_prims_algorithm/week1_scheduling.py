

def make_list_from_data():
    """
    Reads data from txt-file and returns list of 10.000 tuples (job_weight, job_length)
    """
    fh = open('data.txt')
    data = fh.read()
    data_lines = data.split('\n')
    data_lines = data_lines[1:-1]
    job_info = []
    for line in data_lines:
        job = line.split()
        job_info.append((int(job[0]), int(job[1])))
    return job_info


def exercise_1():
    """
    Your task in this problem is to run the greedy algorithm that schedules jobs in decreasing order of the
    difference (weight - length). Recall from lecture that this algorithm is not always optimal. IMPORTANT: if
    two jobs have equal difference (weight - length), you should schedule the job with higher weight first.
    Beware: if you break ties in a different way, you are likely to get the wrong answer. You should report
    the sum of weighted completion times of the resulting schedule --- a positive integer --- in the box below.
    """
    job_info = make_list_from_data()
    #job_info = [(3,5), (1,2)]
    #job_info = [(1, 2), (1,3), (1,4)]
    lst = []
    for job in job_info:
        weight = job[0]
        length = job[1]
        lst.append((weight - length, weight, length))
    lst.sort(reverse = True)
    weighted_sum = 0
    completion_time = 0
    for job in lst:
        weight = job[1]
        length = job[2]
        completion_time += length
        weighted_sum += weight*completion_time
    print "Calculated optimal schedule has weighted sum", weighted_sum
    return weighted_sum
#exercise_1()


def exercise_2():
    """
    Your task now is to run the greedy algorithm that schedules jobs (optimally) in decreasing order of the
    ratio (weight/length). In this algorithm, it does not matter how you break ties. You should report the
     sum of weighted completion times of the resulting schedule --- a positive integer --- in the box below.
     """
    job_info = make_list_from_data()
    #job_info = [(3,5), (1,2)]
    #job_info = [(1, 2), (1,3), (1,4)]
    lst = []
    for job in job_info:
        weight = job[0]
        length = job[1]
        lst.append((weight/float(length), weight, length))
    lst.sort(reverse = True)
    weighted_sum = 0
    completion_time = 0
    for job in lst:
        length = job[2]
        weight = job[1]
        completion_time += length
        weighted_sum += weight*completion_time
    print "Calculated optimal schedule has weighted sum", weighted_sum
    return weighted_sum
#exercise_2()

print (exercise_2()/float(exercise_1()))
