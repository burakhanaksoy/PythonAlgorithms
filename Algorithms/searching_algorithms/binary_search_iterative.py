# To implement binary search (Iterative), the data list we are looking for should be sorted.. IMPORTANT!
data = [1, 2, 4, 5, 8, 11, 12, 13, 23, 24, 33, 55, 66, 101]


def binary_search(data, target):
    low = 0
    high = len(data) - 1

    mid = (low + high) // 2
    count = 0
    while low <= high:
        count += 1
        if target == data[mid]:
            return True
        elif target < data[mid]:
            high = mid - 1
        elif target > data[mid]:
            low = mid + 1
        mid = (low + high) // 2
    return False


print(binary_search(data, 55))
