class Student:
    school = "Some School"

    def __init__(self, first, last, laptop=None):
        self.first = first
        self.last = last
        self.laptop = laptop

    @classmethod
    def get_school(cls):
        return cls.school

    @property
    def full_name(self):
        return f'{self.first} {self.last}'

    @classmethod
    def from_string(cls, name_string):
        first, last = name_string.split('-')
        return cls(first, last)

    def add_laptop(self, laptop):
        self.laptop = laptop

    def show(self):
        print(
            f'School : {self.get_school()}\nInfo: {self.first, self.last, self.laptop}')

    class Laptop:
        def __init__(self, brand, ram, cpu):
            self.brand = brand
            self.ram = ram
            self.cpu = cpu

        def show(self):
            print(f'{self.brand, self.ram, self.cpu}')

        def __repr__(self):
            return f'{self.brand, self.ram, self.cpu}'


laptop1 = Student.Laptop('HP', '8GB', 'i5')
student1 = Student('Burakhan', 'Aksoy', laptop1)
student1.show()

student2 = Student.from_string('Ahmet-Bindere')
student2.show()
student2.add_laptop(laptop1)
student2.show()
print(student1.full_name)
