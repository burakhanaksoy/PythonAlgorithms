# Given an array containing None values, fill in the None values with most recent
# non None value in the array

array1 = [1, None, 2, 3, None, None, 5, None, 6, None, None]


def solution(x):
    current_non_none_value = 0
    for index, value in enumerate(x):
        if value is not None:
            current_non_none_value = value
        else:
            x[index] = current_non_none_value
    return x


print(solution(array2))
