from bisect import *
target = 41
arr = [11, 11, 13, 16, 22, 29, 31]


def pairs(arr, target):
    for i, x in enumerate(arr):
        p = bisect_right(arr, target-x, i)
        if p-1 <= i:
            return
        yield x, arr[p-1]


print(*pairs(arr, target))
