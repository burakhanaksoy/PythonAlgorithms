# Radix sort

array = [55, 3, 111, 23, -1, -6, 3421, 0]


def solution(x):
    num_digits = __get_num_digits(x)
    sorted_array = radix(x, num_digits)
    return sorted_array


def __get_num_digits(A):
    max_digit = len(str(A[0]))
    for num in A:
        char = str(num)
        if max_digit < len(char):
            max_digit = len(char)
    return max_digit


print(solution(array))
