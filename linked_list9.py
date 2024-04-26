# Insertion into LL

# Insertion at the head
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:  # till it becomes null
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end='->')
            current = current.next
        print('None')

    def insert_into_head(self, insert_value):
        new_node = Node(insert_value)
        new_node.next = self.head
        self.head = new_node

    def insert_at_tail(self, insert_tail_value):
        new_node = Node(insert_tail_value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def insert_at_k(self, k, data):
        if k < 0:
            print('Invalid position')
            return

        new_node = Node(data)
        if k == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        count = 0
        while current and count < k - 1:
            current = current.next
            count += 1

        if current is None:
            print('Position out of Range')
        else:
            new_node.next = current.next
            current.next = new_node


arr = [3, 5, 1, 4, 50, 80]
ll = LinkedList()

for data in arr:
    ll.append(data)

# ll.insert_into_head(23)
# ll.display()

ll.insert_at_tail(12)
ll.display()

ll.insert_at_k(2, 45)
ll.display()
