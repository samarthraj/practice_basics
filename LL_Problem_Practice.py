# To Find middle of a linked list
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

    def findMiddleNode(self):
        slow_pointer = self.head
        fast_pointer = self.head
        while fast_pointer != None and fast_pointer.next != None:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
        self.head = slow_pointer
        return

    def reverse_ll(self):
        current = self.head
        prev = None
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
        return


head = [1, 2, 3, 4, 5]
ll = LinkedList()

for data in head:
    ll.append(data)

ll.display()
# ll.findMiddleNode()
# ll.display()

ll.reverse_ll()
ll.display()
