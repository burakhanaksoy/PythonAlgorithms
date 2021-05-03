from linked_list import LinkedList


class NoElementException(Exception):
    pass


class Stack(LinkedList):
    def __init__(self):
        super().__init__()

    def push(self, data):
        super().append(data)

    def pop(self):
        # if not super()._pop() == None:
        return super()._pop()
        # raise NoElementException("No element in the stack...")

    def show(self):
        super().show()

    def peek(self):
        print(super()._peek())
