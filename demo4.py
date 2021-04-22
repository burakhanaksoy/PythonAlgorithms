class Student:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        result = self.m1 + other.m1
        return result

    def __gt__(self, other):
        s1 = self.m1 + self.m2
        s2 = other.m1 + other.m2

        if s1 > s2:
            return True
        return False

    def __str__(self):
        return f'{id(self)}'


burak = Student(12, 22)
ahmet = Student(12, 22)

print(burak + ahmet)
print(burak.__add__(ahmet))

if burak > ahmet:
    print('Burak wins!')
elif ahmet > burak:
    print('Ahmet wins!')
else:
    print('Equal')

print(burak)
