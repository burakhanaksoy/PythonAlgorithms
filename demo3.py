class Compiler:
    def __init__(self, name):
        self.name = name

    def execute(self):
        print("compiling...")
        print("running...")

    @property
    def info(self):
        print(f'{self.name} compiler')


class PyCharm(Compiler):
    def __init__(self, name):
        super().__init__(name)

    def execute(self):
        print("Spell checking...")
        print("compiling...")
        print("running...")


class Computer:

    def __init__(self, brand, ram, cpu):
        self.brand = brand
        self.ram = ram
        self.cpu = cpu

    def execute(self, ide):
        ide.execute(ide)


toshiba = Computer('Toshiba', 8, 'i5')
toshiba.execute(PyCharm)

pycharm = PyCharm('PyCharm')
pycharm.info
