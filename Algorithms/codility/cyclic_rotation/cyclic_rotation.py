A = []
K = 5


def solution(A, K):
    if len(A) == 0:
        return []
    new_list = []
    if K % len(A) == 0:
        return A
    for i in range(K):
        new_list.append(A[-K + i])
    for j in range(1,K+1):
        del A[-1]
    new_list.extend(A)

    return new_list


print(solution(A, K))
