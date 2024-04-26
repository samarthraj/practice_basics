# Convert an array into Linked List
# Print the length of the linked list
# To check if a given value is present in LL or not

# deletion of head and
# deletion of a node in LL
# deletion of a tail in LL
# delete the kth element of a LL

# first we define a Node
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    # appending one by one
    def append(self, data):
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
        while current:
            print(current.data, end='->')
            current = current.next
        print('None')

    def length_of_ll(self):
        ct = 0
        current = self.head
        while current:
            ct += 1
            current = current.next
        print(ct)

    def check_value_is_present(self, val):
        current = self.head
        while current:
            if current.data == val:
                return ('Present')
            current = current.next
        return ('Not Present')

    def delete(self, del_val):
        if self.head is None:
            return

        if self.head.data == del_val:
            # if its first only head move to the next one
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.data == del_val:
                current.next = current.next.next
                return
            current = current.next

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

    def delete_kth_element(self, k):
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
        # just checking if this is the last node
        if current is None:
            return

        prev.next = current.next


arr = [2, 4, 6, 7]
ll = LinkedList()

for data in arr:
    ll.append(data)

ll.display()
ll.length_of_ll()
print(ll.check_value_is_present(41))

# ll.delete(4)
# ll.delete_tail()
ll.display()

ll.delete_kth_element(78)
ll.display()
