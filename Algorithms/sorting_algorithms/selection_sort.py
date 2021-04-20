# sort an array in an ascending order
array = [3, 4, 2, 5, 4, 6, -2]


# def solution(array):
#     for num in array:
#         for i in range(len(array) - 1):
#             if array[i] > array[i+1]:
#                 array[i], array[i+1] = array[i+1], array[i]
#     return array


def solution(array):
    for i in range(len(array)-1):
        current_min = array[i]
        for j in range(i+1, len(array)):
            if current_min > array[j]:
                array[i], array[j] = array[j], array[i]

    return array


print(solution(array))
