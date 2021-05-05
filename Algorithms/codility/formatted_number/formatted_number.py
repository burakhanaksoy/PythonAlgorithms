def FormattedNumber(strArr):
    my_str = strArr[0]
# check multiple dots
    my_list = my_str.split('.')
    if len(my_list) > 2:
        return 'false'
    # get rid of commas and first digit and decimal digits and verify
    del my_list[len(my_list)-1]
    new_str = ''
    for char in my_list:
        new_str += char
    my_list = new_str.split(',')
    del my_list[0]
    for elem in my_list:
        if len(elem) < 3:
            return 'false'
    return 'true'
    # code goes here
    return strArr


# keep this function call here
print(FormattedNumber(["0.0"]))
