# Create a function that takes a number num and returns its length.

def number_length(num):
    if num != None:
        count = 1
        val = num
        while(val // 10 != 0):
            count += 1
            val = val // 10
        return count

print(number_length(392))
