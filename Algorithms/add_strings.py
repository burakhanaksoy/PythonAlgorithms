
# Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.

# Notes:
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.

def solution(x, y):
    result1, result2 = 0, 0
    for digit in x:
        result1 *= 10
        for d in '0123456789':
            result1 += digit > d

    for digit in y:
        result2 *= 10
        for d in '0123456789':
            result2 += digit > d

    return result1 + result2


print(solution('364', '1836'))
