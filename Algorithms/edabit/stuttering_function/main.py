# Write a function that stutters a word as if someone is struggling to read it.
# The first two letters are repeated twice with an ellipsis ... and space after each,
# and then the word is pronounced with a question mark ?.

word = 'hello'


def stutter(word):
    first_two = word[:2] + '... '

    result = first_two * 2 + word + '?'
    return result


print(stutter(word))
