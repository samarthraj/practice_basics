# Convert an array to linked List - Done
# Check if a given value is present in linked list or not
# length_of_linked_list

# first we define the node
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

# we have the LL class in which its empty first with only head pointing to none


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        # check if head is null or not
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end='->')
            current = current.next
        print('None')

    def check_value(self, value):
        current = self.head
        while current:  # i.e. not null
            if current.data == value:
                return ('Yes Present')
            current = current.next
        return ('Not Present')

    def length_of_array(self):
        current = self.head
        ct = 0
        while current:  # not pointing towards null
            ct += 1
            current = current.next
        return ct


arr = [2, 4, 6, 8, 10, 67, 5]
linked_list = LinkedList()

for data in arr:
    linked_list.append(data)

linked_list.display()

print(linked_list.check_value(4))

print(linked_list.length_of_array())
