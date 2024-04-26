# Reverse a ll

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
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current != None:
            print(current.data, end='->')
            current = current.next
        print('None')

    # In order to reverse a LL we use the optimised aproach here instead of the brute force once say we use another
    # ds which uses space - such as a stack and use that to reverse it.
    # here we have to play around with the links and reverse it
    def reverse_ll(self):
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev


head = [1, 2, 3, 4, 5, 6]
ll = LinkedList()

for data in head:
    ll.append(data)

ll.display()

ll.reverse_ll()
ll.display()
