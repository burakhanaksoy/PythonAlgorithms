# Given an array nums, write a function to move all zeroes to the end of it while maintaining
# the relative order of the non-zero elements.

array1 = [0, 1, 0, 3, 12]
array2 = [1, 7, 0, 0, 8, 0, 10, 12, 0, 4]


def solution(x):
    my_list = []
    zero_count = 0
    for i in x:
        if i != 0:
            my_list.append(i)
        else:
            zero_count += 1
    for i in range(zero_count):
        my_list.append(0)
    return my_list


print(solution(array2))
