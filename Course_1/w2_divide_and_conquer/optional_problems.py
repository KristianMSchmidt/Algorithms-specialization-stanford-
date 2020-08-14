

def max_of_unimodal_list(my_list):
    if len(my_list)<=3:
        return max(my_list)

    half_len = len(my_list)/2

    left = my_list[half_len - 1]
    right = my_list[half_len]
    print left, right
    if left<right:
        return max_of_unimodal_list(my_list[half_len:])
    else:
        return max_of_unimodal_list(my_list[:half_len])

print max_of_unimodal_list([3,4,5,6,7,8,9,2,1,-1])
