# Convert an array into Linked List
# Print the length of the linked list
# To check if a given value is present in LL or not

# deletion of head and
# deletion of a node in LL
# deletion of a tail in LL
# delete the kth element of a LL

# write a Node
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    # to convert an array we create an append method
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

    # to print the length of ll
    def length_of_ll(self):
        current = self.head
        ct = 0
        while current:
            ct += 1
            current = current.next
        return ct

    def check_val(self, val):
        if self.head is None:
            return

        current = self.head
        while current:
            if current.data == val:
                return ('Present')
            else:
                current = current.next
        return ('Not Present')

    def delete(self, del_val):
        if self.head is None:
            return

        if self.head.data == del_val:
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
        return

    def delete_kth_element(self, k):
        if self.head is None or k < 0:
            return

        if k == 0:
            self.head = self.head.next
            return

        current = self.head
        ct = 0
        prev = None
        while current and ct < k:
            prev = current
            current = current.next
            ct += 1

        if current is None:
            return

        prev.next = current.next


arr = [2, 3, 4, 5]
ll = LinkedList()

for data in arr:
    ll.append(data)

ll.display()
print(ll.length_of_ll())

print(ll.check_val(12))

# ll.delete(4)
# ll.delete_tail()
ll.delete_kth_element(13)
ll.display()
