# Given an integer, return the integer with reversed digits.
# Note: The integer could be either positive or negative.

def solution(x):
    y=str(x)
    if y[0] == '-':
        y = y[1::]
        return int(f'-{y[::-1]}')
    else:
        return int(f'{y[::-1]}')


# print(solution(123456789))