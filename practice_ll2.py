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


# there is a node class with data and the next
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
            while current.next is not None:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end='->')
            current = current.next
        print('None')

    def length_of_ll(self):
        ct = 0
        current = self.head
        while current is not None:
            ct += 1
            current = current.next
        return ct

    def check_if_node_present(self, value):
        current = self.head
        while current is not None:
            if current.data == value:
                return ('Present')
            current = current.next
        return ('Not Present')

    def delete_node(self, del_value):
        if self.head is None:
            return

        if self.head.data == del_value:
            self.head = self.head.next
            return

        current = self.head
        while current.next is not None:
            if current.next.data == del_value:
                current.next = current.next.next
                return
            current = current.next
        return

    def delete_tail(self):
        if self.head is None:
            return

        if self.head.next is None:
            self.head = None
            return

        current = self.head
        while current.next.next is not None:
            current = current.next
        current.next = None
        return

    def delete_kth_element(self, k):
        if self.head is None or k < 0:
            print('Invalid K')
            return

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

    def insert_at_tail(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        if self.head.next is None:
            self.head.next = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node
        return

    def insert_at_k(self, k, data):
        if k < 0:
            raise ValueError('Invalid Position: k should be non-negative')

        new_node = Node(data)

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
            raise IndexError(
                'Position out of Range: k is greater than the size of the list')
        else:
            new_node.next = current.next
            current.next = new_node
            return


arr = [1, 5, 2, 7, 20]
ll = LinkedList()

for data in arr:
    ll.append(data)

ll.display()
# print(ll.length_of_ll())

# print(ll.check_if_node_present(7))

# ll.delete_node(100)
# ll.display()

# ll.delete_kth_element(10)

ll.insert_at_k(-9, 200)
ll.display()
