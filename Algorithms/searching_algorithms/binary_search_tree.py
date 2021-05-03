class Node:
    def __init__(self, data=None):
        self.data = data
        self.child_node_right = None
        self.child_node_left = None


class BinarySearchTree:
    def __init__(self):
        self.head = Node()

    def insert(self, data):
        cur_node = self.head
        if cur_node.data == None:
            cur_node = Node(data)
            self.head = cur_node
        else:
            self._insert(data, cur_node)

    def _insert(self, data, cur_node):
        if cur_node.data < data:
            if cur_node.child_node_right == None:
                cur_node.child_node_right = Node(data)
            else:
                self._insert(data, cur_node.child_node_right)
        elif cur_node.data > data:
            if cur_node.child_node_left == None:
                cur_node.child_node_left = Node(data)
            else:
                self._insert(data, cur_node.child_node_left)
        else:
            pass
            # print("Value already in the tree...")

    def print_tree(self):
        if self.head.data != None:
            self._print_tree(self.head)

    def _print_tree(self, cur_node):
        if cur_node != None:
            self._print_tree(cur_node.child_node_left)
            print(cur_node.data)
            self._print_tree(cur_node.child_node_right)

    def height(self):
        if self.head.data != None:
            return self._height(self.head)
        else:
            return 0

    left_count = 0
    right_count = 0

    def _height(self, cur_node):
        # Left sub-tree
        if cur_node.child_node_left != None:
            self.left_count += 1
            self._height(cur_node.child_node_left)
        # Right sub-tree
        if cur_node.child_node_right != None:
            self.right_count += 1
            self._height(cur_node.child_node_right)
        if self.right_count > self.left_count:
            return self.right_count + 1
        return self.left_count + 1

    def search(self, data):
        if self.head.data != None:
            return self._search(data, self.head)

    def _search(self, data, cur_node):
        try:
            if data == cur_node.data:
                return True
            elif data < cur_node.data:
                return self._search(data, cur_node.child_node_left)
            elif data > cur_node.data:
                return self._search(data, cur_node.child_node_right)
        except AttributeError:
            return False


def fill_tree(tree, min_num=0, max_length=1000):
    from random import randint
    for _ in range(max_length):
        tree.insert(randint(min_num, max_length))


tree = BinarySearchTree()
fill_tree(tree, max_length=7)
tree.print_tree()
print(tree.height())
print(tree.search(3))
print(tree.search(1))
