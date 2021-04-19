# Given a string, find the first non-repeating character in it and return its index.
# If it doesn't exist, return -1. # Note: all the input strings are already lowercase.

def solution(x):

    sentence = x
    new_sent = sentence.replace(' ', '')
    sent_list = []
    for char in new_sent:
        sent_list.append(char)

    my_unique_list = []
    duplicate_list = []
    for char in new_sent:
        if char not in my_unique_list:
            my_unique_list.append(char)
        else:
            duplicate_list.append(char)

    last_sent = ''
    for char in sentence:
        if char not in duplicate_list:
            last_sent += char
        else:
            last_sent += ' '
    # Check if last_sent contains something else than space
    set_check = set(last_sent)
    if not (len(set_check) != 1 and set_check.pop() != ' '):
        return -1
    # Find the first non-space element and return its index
    counter = 0
    for char in last_sent:
        if char != ' ':
            break
        else:
            counter = counter + 1
    return counter


print(solution('alphabet'))
print(solution('barbados'))
print(solution('crunchy'))