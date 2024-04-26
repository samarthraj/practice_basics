# Convert an array into Linked List
# Print the length of the linked list
# To check if a given value is present in LL or not

# deletion of head and
# deletion of a node in LL
# deletion of a tail in LL

# First you should have define a node
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

# we define the LL here which has an empty head or pointing to none


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

    def length_of_ll(self):
        ct = 0
        current = self.head
        while current:
            ct += 1
            current = current.next
        return ct

    def check_value(self, value):
        current = self.head
        while current:
            if current.data == value:
                return ('Yes, Present')
            current = current.next
        return ('Not Present')

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

    def display(self):
        current = self.head
        while current:
            print(current.data, end='->')
            current = current.next
        print('None')

    def delete_Tail(self):
        if self.head is None:
            return

        if self.head.next is None:
            self.head = None
            return

        current = self.head
        while current.next.next:
            current = current.next
        current.next = None

    def delete_kth_element(self, k):
        # first check if the head is null
        if self.head is None or k < 0:
            return

        if k == 0:
            self.head = self.head.next
            return

        current = self.head
        prev = None
        ct = 0
        while current and ct < k:
            prev = current
            current = current.next
            ct += 1

        if current is None:
            return

        prev.next = current.next


arr = [2, 4, 6, 7, 5, 7, 2]
ll = LinkedList()

for data in arr:
    ll.append(data)

# print(ll.length_of_ll())
# print(ll.check_value(5))

# ll.delete_Tail()
ll.delete_kth_element(0)
ll.display()
