class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = Node()

    def append(self, data):
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
        cur_node.next = Node(data)

    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elems.append(cur_node)
        print(elems)

    @property
    def length(self):
        count = 0
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            count += 1
        return count

    def remove(self, index):
        cur_node = self.head
        prev_node = self.head
        cur_idx = 0
        while cur_node.next != None:
            cur_node = cur_node.next
            if cur_idx == index:
                prev_node.next = cur_node.next
                break
            cur_idx += 1
            prev_node = cur_node

    def get(self, index):
        cur_idx = 0
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            if cur_idx == index:
                return cur_node.data
            cur_idx += 1

linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)
linked_list.display()
linked_list.remove(0)
linked_list.display()