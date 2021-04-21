# Bubble sort

# Kabarcik icin bir index lazim
# ikili comparison icin baska bir index lazim

array = [2, 1, 6, 1, 3, -2,-4, 9, 7]


def solution(array):
    for num in array:
        for i in range(len(array)-1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
    return array


print(solution(array))
