# Convert an array into Linked List
# Print the length of the linked list
# To check if a given value is present in LL or not

# deletion of head and
# deletion of a node in LL
# deletion of a tail in LL
# delete the kth element of a LL

# define a node
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
            while current.next:  # till it becomes null
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end='->')
            current = current.next
        print('None')

    def length_of_ll(self):
        current = self.head
        ct = 0
        while current:
            ct += 1
            current = current.next
        return ct

    def value_check(self, value):
        if self.head is None:
            return

        current = self.head
        while current:
            if current.data == value:
                return ('Value is Present')
            else:
                current = current.next
        return ('Value not Present')

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

        if k == 0:  # means 1st element
            self.head = self.head.next
            return

        current = self.head
        prev = None
        count = 0
        while current and count < k:
            prev = current
            current = current.next
            count += 1

        if current is None:
            return

        prev.next = current.next


arr = [3, 5, 1, 4, 50, 80]
ll = LinkedList()

for data in arr:
    ll.append(data)

ll.display()
print(ll.length_of_ll())

print(ll.value_check(512))

# ll.delete(50)
# ll.delete_tail()
ll.delete_kth_element(1)
ll.display()
