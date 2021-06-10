def add_suffix(suffix):
    def func(word):
        word += suffix
        return word
    return func


add_ly = add_suffix('ly')
print(add_ly('Careful'))

add_less = add_suffix('less')
print(add_less('Fear'))
