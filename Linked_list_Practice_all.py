# Convert an array into Linked List
# Print the length of the linked list
# To check if a given value is present in LL or not

# deletion of head and
# deletion of a node in LL
# deletion of a tail in LL
# delete the kth element of a LL

# Insertion into LL
# Insertion at the head
# Insertion at the Tail
# Insertion at the kth index

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
            return
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end='->')
            current = current.next
        print('None')

    def length_of_array(self):
        ct = 0
        current = self.head

        while current is not None:
            current = current.next
            ct += 1
        return ct

    def check_value(self, value):
        if self.head is None:
            return

        current = self.head
        while current is not None:
            if current.data == value:
                return "Present"
            current = current.next
        return "Not Present"

    def delete_from_head(self):
        if self.head is None:
            return

        if self.head.next is not None:
            self.head = self.head.next
            return

    def delete_from_tail(self):
        if self.head is None:
            return

        current = self.head
        while current.next.next is not None:
            current = current.next
        current.next = None

    def delete_value(self, value):
        if self.head.data == value:
            self.head = self.head.next
            return

        current = self.head
        while current.next is not None:
            if current.next.data == value:
                current.next = current.next.next
                return
            current = current.next
        return

    def delete_from_k(self, k):
        if self.head is None or k < 0:
            return ('Invalid')

        if k == 0:
            self.head = self.head.next
            return

        current = self.head
        prev = None
        ct = 0
        while current is not None and ct < k:
            prev = current
            current = current.next
            ct += 1

        if current is None:
            return
        else:
            prev.next = current.next

    def insert_into_head(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        if self.head.next is not None:
            new_node.next = self.head
            self.head = new_node
            return

    def insert_into_tail(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node
        return

    def insert_into_k(self, data, k):
        new_node = Node(data)
        if k < 0:
            return "Invalid"

        if k == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        ct = 0
        while current is not None and ct < k - 1:
            current = current.next
            ct += 1

        if current is None:
            return "Invalid error"
        else:
            new_node.next = current.next
            current.next = new_node
            return


arr = [1, 2, 3, 4, 5]
ll = LinkedList()

for data in arr:
    ll.append(data)

ll.display()
# print(ll.length_of_array())
# print(ll.check_value(5))

# ll.delete_from_head()
# ll.display()
# ll.delete_from_tail()
# ll.display()
# ll.delete_value(20)
# ll.delete_from_k(40)
# ll.insert_into_head()
# ll.insert_into_tail(7)
ll.insert_into_k(7, 1)
ll.display()
