# deletion of head and
# deletion of a node in LL
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

# next we define the LL class itself which contains the head pointer only initially


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

    def delete(self, del_value):
        if self.head is None:
            return

        if self.head.data == del_value:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.data == del_value:
                current.next = current.next.next
                return
            current = current.next


arr = [4, 5, 1, 7, 10]
linked_list = LinkedList()

for data in arr:
    linked_list.append(data)

# linked_list.length_of_linked_list()

# value = 12
# res = linked_list.check_if_present(value)
# print(res)

del_value = 4
linked_list.delete(del_value)

linked_list.display()
