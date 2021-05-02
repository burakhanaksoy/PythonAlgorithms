# Recursive approach is based on function calling itself.. It's not recommended due to making code less readable
#  and harder to maintain and debug.

def binary_search_recursive(data, target, low, high):
    mid = (low + high) // 2
    if low > high:
        return False
    if target == data[mid]:
        return True
    elif target < data[mid]:
        binary_search_recursive(data, target, low, mid-1)
    elif target > data[mid]:
        binary_search_recursive(data, target, low + 1, high)


data = [1, 2, 4, 5, 8, 11, 12, 13, 23, 24, 33, 55, 66, 101]
print(binary_search_recursive(data, 23, 0, len(data)-1))

# TODO: focus on this... 