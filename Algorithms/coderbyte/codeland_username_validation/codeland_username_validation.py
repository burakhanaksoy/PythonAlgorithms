def CodelandUsernameValidation(strParam):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    accepted_car = letters + '0123456789' + '_'

    if strParam[0] not in letters:
        return 'false'
    elif not 4 < len(strParam) < 25:
        return 'false'
    elif strParam[len(strParam)-1] == '_':
        return 'false'

    for i in strParam:
        if i not in accepted_car:
            return 'false'
    return 'true'


# keep this function call here
# print CodelandUsernameValidation(

print(CodelandUsernameValidation("u__hello_world123*"))
