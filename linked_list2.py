# convert a list to an array in Linked List
# first we have to define a node in a Linked List
# length of the linked List
# Check if a given value is present in linked list or not
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

# next we define the LL class itself which contains the head pointer only initially
# this is a modified script


class LinkedList:
    def __init__(self):
        self.head = None

    # this method checks if the head is pointing to a node or not, i.e. null or not
    # also call the new node here
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            # means the next pointer is not null up until then run the loop
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end='->')
            current = current.next
        print('None')

    def length_of_linked_list(self):
        ct = 0
        current = self.head
        while current:
            ct += 1
            current = current.next
        print(ct)

    def check_if_present(self, value):
        current = self.head
        while current:
            if current.data == value:
                return ("Present")
            current = current.next
        return ("Not Present")


arr = [4, 5, 1, 7, 10]
linked_list = LinkedList()

for data in arr:
    linked_list.append(data)

linked_list.length_of_linked_list()

value = 12
res = linked_list.check_if_present(value)
print(res)
