def LongestWord(sen):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789'
    words = sen.split(' ')
    longest = 0
    result = None
    for word in words:
        count = 0
        for c in word:
            if c in letters:
                count += 1
        if count > longest:
            longest = count
            result = word
    return result


# keep this function call here
print(LongestWord("123456789 98765432"))
