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

    def append_an_array(self, data):
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
        while current is not None:
            print(current.data, end='->')
            current = current.next
        print('None')

    def length_of_ll(self):
        current = self.head
        ct = 0
        while current:
            current = current.next
            ct += 1
        return ct

    def check_if_present(self, val):
        if self.head is None:
            return

        current = self.head
        while current:
            if current.data == val:
                return True
            current = current.next
        return False

    def delete(self, del_val):
        if self.head is None:
            return

        if self.head.data == del_val:
            self.head = self.head.next
            return

        current = self.head
        while current.next is not None:
            if current.next.data == del_val:
                current.next = current.next.next
                return
            current = current.next

    def tail_of_ll(self):
        if self.head is None:
            return

        current = self.head
        while current.next.next is not None:
            current = current.next
        current.next = None
        return

    def delete_kth_element(self, k):
        if self.head is None and k < 0:
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

    def insert_into_tail(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node
        new_node.next = None
        return

    def insert_into_kth_index(self, data, k):
        new_node = Node(data)
        if k < 0:
            raise Exception('Index Error')
        if k == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        prev = None
        ct = 0

        while current is not None and ct < k:
            prev = current
            current = current.next
            ct += 1

        if current is None:
            raise Exception("Position Out of Range")
        else:
            # new_node.next = prev.next or
            new_node.next = current
            prev.next = new_node
            return


arr = [1, 2, 4, 5, 7]
ll = LinkedList()

for data in arr:
    ll.append_an_array(data)

ll.display()
# print(ll.length_of_ll())
# print(ll.check_if_present(20))
# ll.delete(2)
# ll.tail_of_ll()
# ll.display()

# ll.delete_kth_element(5)
# ll.insert_into_head(8)
ll.insert_into_kth_index(80, 3)
ll.display()
