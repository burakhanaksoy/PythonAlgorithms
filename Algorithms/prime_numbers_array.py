# Given k numbers which are less than n, return the set of prime number among them
# Note: The task is to write a program to print all Prime numbers in an Interval.
# Definition: A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
n = 35


def solution(number):
    prime_numbers = []
    for num in range(2, number):
        is_prime = True
        for i in range(2, number):
            if num % i == 0 and num != i:
                is_prime = False
        if is_prime:
            prime_numbers.append(num)
    return prime_numbers


print(solution(n))
