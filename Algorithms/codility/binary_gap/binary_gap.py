def solution(N):
    y = str(bin(N))
    x = y[2::][::-1]
    max_count = 0
    for i in range(len(x)-2):
        counter = 0
        j = i
        if x[i] == '0':
            first_one = False
        else:
            first_one = True
        if first_one:
            while x[j+1] == '0' and j < len(x)-1:
                counter += 1
                j += 1
            if counter > max_count:
                max_count = counter

    return max_count


print(solution(1001))


