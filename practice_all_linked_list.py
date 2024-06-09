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
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node

    def display(self):
        current = self.head
        while current:
            print(current.data, end="->")
            current = current.next
        print(None)

    def length_of_linked_list(self):
        current = self.head
        ct = 0
        while current:
            ct += 1
            current = current.next
        return ct

    def check_val(self, val):
        current = self.head
        while current:
            if current.data == val:
                return ('Value Present')
            current = current.next
        return ('Value Not Present')

    def delete_head(self):
        if self.head is None:
            return ('Head not Present')
        else:
            self.head = self.head.next
            return

    def delete_tail(self):
        if self.head is None:
            return

        if self.head.next is None:
            self.head = None
            return

        current = self.head
        while current.next.next:
            current = current.next
        current.next = None
        return

    def delete_any_node(self, del_val):
        if self.head is None:
            return

        current = self.head
        while current.next:
            if current.next.data == del_val:
                current.next = current.next.next
                return
            current = current.next

    def delete_kth_element(self, k):
        if self.head is None or k < 0:
            return

        if k == 0:
            self.head = self.head.next
            return

        current = self.head
        ct = 0
        prev = None
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
        else:
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
            return
        elif k == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        ct = 0
        # prev = None
        while current is not None and ct < k - 1:
            current = current.next
            ct += 1

        if current is None:
            return
        else:
            new_node.next = current.next
            current.next = new_node
            return


arr = [1, 2, 3, 4, 5]
ll = LinkedList()
for data in arr:
    ll.append(data)

ll.display()
# print(ll.length_of_linked_list())
# print(ll.check_val(2))
# ll.delete_head()
# ll.display()

# ll.delete_kth_element(2)
# ll.display()

# ll.insert_into_head(8)
# ll.display()

ll.insert_into_k(9, 1)
ll.display()
