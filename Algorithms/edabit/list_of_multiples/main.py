# Create a function that takes two numbers as arguments (num, length) and
# returns a list of multiples of num until the list length reaches length.

def list_of_multiples(num, length):
    result = []
    for i in range(1,length + 1):
        result.append(num * i)

    return result


print(list_of_multiples(7, 5))
