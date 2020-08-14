"""
Implementation of Quick Sort with different strategies for chosing pivots. Random pivots are provably best, though.
In particular, this exercise is about counting the number of comparisons when doing quick_sort.
"""
def partition_l(my_list, l, r):
    """
    Partition subrutine to be used by quick sort.
    Partitions my_list[l,r] with respect to pivot my_list[l]
    """
    pivot = my_list[l]
    #print pivot

    i = l + 1
    for j in range(l + 1, r+1):
        #print i, j
        if my_list[j] < pivot:
            if i != j:
                my_list[i], my_list[j] = my_list[j], my_list[i]
            i += 1
    my_list[l], my_list[i-1] = my_list[i-1], my_list[l]

    #right_pivot_pos = i-1
    return my_list, i-1

def partition_median_of_three(my_list, l, r):
    """
    Partition subrutine to be used by quick sort.
    Partitions my_list[l,r] where pivot is chosen as median of first, middle and last element
    """
    m = l + (r - l)/2

    #find pivot position
    num_l, num_m, num_r = my_list[l], my_list[m], my_list[r]
    if (num_l < num_m < num_r) or (num_r < num_m < num_l):
        pivot_pos = m
    elif num_m < num_l < num_r or num_r < num_l < num_m:
        pivot_pos = l
    else:
        pivot_pos = r
    #print "pivot", my_list[pivot_pos]
    # make pivot the first element
    my_list[l], my_list[pivot_pos] = my_list[pivot_pos], my_list[l]

    # use standard partition on new list
    return partition_l(my_list, l, r)

#print partition_median_of_three([3,2,1,0],1,3)

def partition_r(my_list, l, r):
    """
    Partition subrutine to be used by quick sort.
    Partitions my_list[l,r] with respect to pivot my_list[r]
    """
    my_list[l], my_list[r] = my_list[r], my_list[l]
    return partition_l(my_list, l, r)


def test():
    result = partition_r([2,3,1,-1,-2,0], 0, 5)
    print result
#test()

number_of_comparisons = 0
def quick_sort(my_list, l, r):
    """
    Quick sort
    """
    global number_of_comparisons

    if r == l:
        return my_list

    #choose method for choosing pivot
    #partitioned, right_pivot_pos = partition_l(my_list, l, r)
    partitioned, right_pivot_pos = partition_r(my_list, l, r)
    #partitioned, right_pivot_pos = partition_median_of_three(my_list, l, r)

    number_of_comparisons += (r-l)

    left_part = quick_sort(partitioned, l, max(l, right_pivot_pos - 1))
    right_part = quick_sort(left_part, min(right_pivot_pos + 1, r), r)

    return my_list

#print quick_sort([9,-1,2,8,18],0,4)
#print number_of_comparisons

def run_quick_sort(my_list):
    return quick_sort(my_list, 0, len(my_list)-1)

def import_data():
    import urllib2
    URL = "https://d3c33hcgiwev3.cloudfront.net/_32387ba40b36359a38625cbb397eee65_QuickSort.txt?Expires=1514678400&Signature=UbQM4sANM7dVrQtz0DJ1850w5dkkwl-eJtx0ZC7Jz7KHjiVA4WxrBVeAUIaf76DAvLl7jPjrOrix4mvUu1Noti31wozK~70jT22V-uPuTr2YrWSCW4a1cRgEUcvHMK-necnAB1l5Kon6Bi1dc7N0dU6cywsat3EyPNOdDijaxW0_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A"
    data_file = urllib2.urlopen(URL)
    data = data_file.read()
    data_lines = data.split('\n')
    data_lines = data_lines[:-1]
    data_lines = [int(number) for number in data_lines]
    print "Data has been loaded and cleaned"
    print run_quick_sort(data_lines)[-10:]
    print "Total number of comparisons made under recursive partitioning:", number_of_comparisons
import_data()
