# Convert an array to linked List
# First we have to define a node in Linked List, initially the next is pointing to null
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

# practicing to commit modified files
# next we define the actual linked list which has head pointing to null and the linked list is empty initially


class LinkedList:
    def __init__(self):
        self.head = None

    # next we have to create a method which checks if the head is pointing to empty or not,
    # i.e. if there is a node or not.
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:  # meaning current.next null ago tanaka
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end='->')
            current = current.next
        print('None')


arr = [2, 3, 5, 6]
# creating an object of ll class
linked_list = LinkedList()
for data in arr:
    linked_list.append(data)

linked_list.display()
