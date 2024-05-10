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

# contains the head of the linked list


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
            current = current.next
            ct = ct + 1
        return ct

    def check_value_in_ll(self, value):
        current = self.head
        while current is not None:
            if current.data == value:
                return ('Value Present')
            current = current.next
        return ('Value not Present')

    def delete(self, value):
        if self.head is None:
            return

        # if self.head.next is not None:
        #     self.head = self.head.next
        #     return

        current = self.head
        while current.next is not None:
            if current.next.data == value:
                current.next = current.next.next
                return  # we have finished deleting it so return from the loop
            current = current.next

    def delete_tail(self):
        if self.head is None:
            return

        if self.head.next is None:
            self.head = None
            return

        current = self.head
        while current.next.next is not None:
            current = current.next
        current.next = current.next.next

    def delete_at_kth_index(self, k):
        if self.head is None or k < 0:
            raise Exception("Index error")

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

        # This line simply says if we give an input k which is more than the length of arr it should return without throwing an error.
        if current is None:
            return

        prev.next = current.next

    def insert_into_head_ll(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        if self.head.next is not None:
            new_node.next = self.head
            self.head = new_node
            return

    def insert_into_tail_ll(self, data):
        new_node = Node(data)
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node
        # new_node.next = None
        return

    def insert_into_kth_element_ll(self, k, data):
        new_node = Node(data)
        if k < 0:
            raise Exception("Index error")

        if k == 0:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        # prev = None
        ct = 0
        while current is not None and ct < k - 1:
            # prev = current
            current = current.next
            ct += 1
        if current is None:
            return
        # new_node.next = current
        # prev.next = new_node

        new_node.next = current.next
        current.next = new_node


arr = [1, 4, 2, 9, 5]
# create an object of the class
ll = LinkedList()

for data in arr:
    ll.append(data)


ll.display()
# print(ll.length_of_ll())
# print(ll.check_value_in_ll(51))

# ll.delete(9)
# ll.display()

# ll.delete_tail()
# ll.display()

# ll.delete_at_kth_index(5)
# ll.display()

# ll.insert_into_head_ll(3)
# ll.display()

# ll.insert_into_tail_ll(6)
# ll.display()

ll.insert_into_kth_element_ll(2, 8)
ll.display()
