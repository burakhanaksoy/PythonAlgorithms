class A:
    def __init__(self):
        print('Class A constructor called')

    def feature1(self):
        print('Feature 1-A')

    def feature2(self):
        print('Feature 2')


class B:
    def __init__(self):
        print('Class B constructor called')

    def feature1(self):
        print('Feature 1-B')

    def feature4(self):
        print('Feature 4')


class C(A,B):
    def __init__(self):
        super().__init__()
        print('Class C constructor called')

    def feature5(self):
        print('Feature 5')


objC = C()
objC.feature1()
