# Write a function that converts a dictionary into a list,
# where each element represents a key-value pair in the form of a list.
# Sort the list alphabetically by key.

# def to_list(dictionary):
#     my_list = []

#     for k, v in dictionary.items():
#         my_list.append([k, v])

#     return sorted(my_list)

def to_list(dct):
    return sorted([[key, val] for key, val in dct.items()])


print(to_list({"shrimp": 15, "tots": 12}))

my_dict = {"shrimp": 15, "tots": 12}

print(sorted([list(i) for i in my_dict.items()]))
