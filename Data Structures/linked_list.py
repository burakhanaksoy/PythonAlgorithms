class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node()

    def append(self, data):
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
        cur_node.next = Node(data)

    def remove(self, data):
        cur_node = self.head
        prev_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            if cur_node.data == data:
                prev_node.next = cur_node.next
                break
            prev_node = cur_node

    def size(self):
        cur_node = self.head
        self.count = 0
        while cur_node.next != None:
            cur_node = cur_node.next
            self.count += 1
        return self.count

    def get(self, index):
        cur_node = self.head
        my_list = []
        while cur_node.next != None:
            cur_node = cur_node.next
            my_list.append(cur_node.data)
        for i in my_list:
            if i == my_list[index]:
                return i

    def show(self):
        node_list = []
        cur_node = self.head.next
        while cur_node != None:
            node_list.append(cur_node.data)
            cur_node = cur_node.next
        print(node_list)

    def _pop(self):
        cur_node = self.head
        prev_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            if cur_node.next == None:
                prev_node.next = cur_node.next
            prev_node = cur_node
        return prev_node.data

    def _peek(self):
        cur_node = self.head
        while cur_node.next !=None:
            cur_node = cur_node.next
        return cur_node.data
