import random


def quicksort(nums):
    if len(nums) <= 1:
        return nums
    smaller, equal, larger = [], [], []
    pivot = nums[random.randint(0, len(nums)-1)]

    for x in nums:
        if x < pivot:
            smaller.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            larger.append(x)

    return quicksort(smaller) + equal + quicksort(larger)


def random_array_generator():
    my_list = []
    for _ in range(10):
        my_list.append(random.randint(-100, 100))
    return my_list


my_list = random_array_generator()
print(quicksort([3, 1, 0, 11]))
