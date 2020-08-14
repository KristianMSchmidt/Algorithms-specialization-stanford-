"""
Divide and Conquer algorithm to count number of invertions in given list of distinct integers. It's not really important, that the
integers are distinct - I just made it that way for sake of clarity.
"""
import urllib2

def merge_and_count_split(list_1, list_2, len_list_1, len_list_2):
    """
    Takes two sorted lists (distinct integers), returns merge sorted list and number of split invertions.
    """
    answer = []
    index_1 = 0
    index_2 = 0
    num_split = 0

    while index_1 < len_list_1 and index_2 < len_list_2:
        num1 = list_1[index_1]
        num2 = list_2[index_2]
        if num1 < num2:
            answer.append(num1)
            index_1 += 1
        else:
            answer.append(num2)
            index_2 += 1
            num_split += len_list_1 - index_1

    if index_1 == len_list_1:
        return answer + list_2[index_2:], num_split

    else:
        return answer + list_1[index_1:], num_split

#print merge_and_count_split([2,100],[1,11,12,14],2,4)

def sort_and_count_inv(my_list, length):
    """
    Takes a list of length, returns sorted list and number of invertions in list.
    """
    #base case:
    if length <= 1:
        return (my_list, 0)

    len_first_half = length/2
    len_second_half = length - len_first_half
    first_half = my_list[:len_first_half]
    second_half = my_list[len_first_half:]

    sorted_first_half, count_1 = sort_and_count_inv(first_half, len_first_half)
    sorted_second_half, count_2 = sort_and_count_inv(second_half, len_second_half)
    sorted_list, num_split_inv = merge_and_count_split(sorted_first_half, sorted_second_half, len_first_half, len_second_half)

    total_invertions= count_1 + count_2+ num_split_inv

    return sorted_list, total_invertions

#print sort_and_count_inv([1,2,3,4,5,6,-1,10,0],9)


###QUESTION
URL= "https://d3c33hcgiwev3.cloudfront.net/_bcb5c6658381416d19b01bfc1d3993b5_IntegerArray.txt?Expires=1514678400&Signature=aSOXlexxIxG1wz5~zqBfGvds7LXiQX5wBV25fbJ7u~xTjyt5Fnc1JcAN4XNyJrBPiMobwGOsrfwWHvWdFRFlSIg8~M57-ZpHLFekbgmydt~StuEk2rI-KLb79iBUrtHlE0VBm4ZwdIS4Tqeww5rP4wC5Rry-1g4prT14hKpsQBE_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A"
data_file = urllib2.urlopen(URL)
data = data_file.read()
data_lines = data.split('\n')
data_lines = data_lines[:-1]
data_lines = [int(number) for number in data_lines]
print "Data has been loaded and cleaned"
answer = sort_and_count_inv(data_lines, len(data_lines))[1]
print "Number of inversions:", answer

print "Maximum possible number of invertion is approximately: ", (100000-1)*(100000-2)/2
print float(answer)/((100000-1)*(100000-2)/2)*100, "%"
