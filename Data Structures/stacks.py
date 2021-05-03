class stack:
    def __init__(self):
        self.my_stack = []

    def add(self, data):
        self.my_stack.append(data)

    def pop(self):
        obj = self.my_stack[len(self.my_stack)-1]
        self.my_stack.remove(obj)
        return obj

    def push(self, data):
        self.my_stack.append(data)

    def peek(self):
        try:
            if self.my_stack[len(self.my_stack)-1] != None:
                print(self.my_stack[len(self.my_stack)-1])
        except IndexError:
            raise Exception('No item in the list.')

    def size(self):
        self.count = 0
        while True:
            try:
                if self.my_stack[self.count] != None:
                    self.count += 1
            except IndexError:
                return self.count

    def show(self):
        print(self.my_stack)
