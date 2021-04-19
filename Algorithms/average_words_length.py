# For a given sentence, return the average word length.
# Note: Remember to remove punctuation first.

def solution(x):
    my_sentence = ''
    sentence = str(x)
    punctuations = """!()-[]{};:'"\,<>./?@#$%^&*_~"""
    for char in sentence:
        if char not in punctuations:
            my_sentence = my_sentence + char

    spaces_removed_list = my_sentence.split(' ')
    sum = 0
    for element in spaces_removed_list:
        sum = sum + len(element)
    average = sum / len(spaces_removed_list)
    return round(average, 2)
    # for item in spaces_removed_list:


print(solution("I need to work very hard to learn more about algorithms in Python!"))
