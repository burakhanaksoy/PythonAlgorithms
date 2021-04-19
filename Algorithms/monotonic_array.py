# An array is monotonic if it is either monotone increasing or monotone decreasing.
# An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone decreasing if for all i <= j, A[i] >= A[j].
# Return true if and only if the given array A is monotonic.

def solution(x):
    check1 = True
    check2 = True

    for j in range(len(x)-1):
        if x[j] >= x[j+1]:
            pass
        else:
            check1 = False
    for i in range(len(x)-1):
        if x[i] <= x[i+1]:
            pass
        else:
            check2 = False
    return check1 or check2


A = [6, 5, 4, 4]
B = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
C = [1, 1, 2, 3, 7]
D = [1,2,3,4,4,6,5]

print(solution(A))
print(solution(B))
print(solution(C))
print(solution(D))
