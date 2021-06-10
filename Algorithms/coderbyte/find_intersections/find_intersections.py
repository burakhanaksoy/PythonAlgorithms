def FindIntersection(strArr):
    set_one = set(strArr[0].split(', '))
    set_two = set(strArr[1].split(', '))

    list1 = sorted(list(set_one & set_two))
    list2 = sorted([int(i) for i in list1])
    list1 = [str(i) for i in list2]
    string1 = ','.join(list1)

    return 'true' if len(string1) != 0 else 'false'


print(FindIntersection(["1, 3, 9, 10, 17, 18", "1, 4, 9, 10"]))
