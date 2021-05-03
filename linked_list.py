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
            if cur_node.data == data:
                prev_node.next = cur_node.next
                break
            prev_node = cur_node
            cur_node = cur_node.next

    def show(self):
        node_list = []
        cur_node = self.head.next
        while cur_node != None:
            node_list.append(cur_node.data)
            cur_node = cur_node.next
        print(node_list)


linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)
linked_list.show()
linked_list.remove(5)
linked_list.show()
