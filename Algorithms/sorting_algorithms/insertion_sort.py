# implement insertion sort

array = [7, 5, 8, 2, 4, 6, 3]


def solution(array):
    for i in range(1, len(array)):
        j = i
        while array[j-1] > array[j] and j > 0:
            array[j-1], array[j] = array[j], array[j-1]
            j -= 1
    return array


print(solution(array))
