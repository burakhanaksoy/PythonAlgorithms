# You prepare a list to send to the insurance company. As you finish, you notice you misformatted it.
# Given a dictionary with at least one key/value pair, convert all the values to numbers.

def convert_to_number(dictionary):
    for key in dictionary.keys():
        dictionary[key] = int(dictionary[key])

    return dictionary

print(convert_to_number({'val':'200','val2':'300'}))