# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    new_list = []
    for num in A:
        if not num in new_list:
            new_list.append(num)
        else:
            new_list.remove(num)
    return new_list[0]


print(solution([1, 2, 3, 1, 2]))
