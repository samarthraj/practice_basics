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

# define a Node
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
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end='->')
            current = current.next
        print('None')

    def length_of_an_array(self):
        current = self.head
        ct = 0
        while current:
            ct += 1
            current = current.next
        return ct

    def check_value_in_ll(self, value):
        if self.head is None:
            return

        current = self.head
        while current:
            if current.data == value:
                return ('Value is Present')
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

    def delete_tail_from_ll(self):
        if self.head is None:
            return

        if self.head.next is None:
            self.head = None
            return

        current = self.head
        while current.next.next:
            current = current.next
        current.next = None

    def delete_kth_element_from_ll(self, k):
        if self.head is None or k < 0:
            return

        if k == 0:
            self.head = self.head.next
            return

        current = self.head
        prev = None
        ct = 0
        while current and ct < k:
            ct += 1
            prev = current
            current = current.next

        if current is None:
            return

        prev.next = current.next

    # def delete_kth_element_from_ll(self, k):
    #     if self.head is None or k < 0:
    #         return

    #     if k == 0:
    #         self.head = self.head.next
    #         return

    #     current = self.head
    #     ct = 0
    #     while current and ct < k - 1:
    #         ct += 1
    #         current = current.next

    #     if current is None or current.next is None:
    #         return

    #     current.next = current.next.next

    def insertion_into_head(self, insert_node):
        new_node = Node(insert_node)
        new_node.next = self.head
        self.head = new_node

    def insertion_into_tail(self, insert_node):
        new_node = Node(insert_node)
        if self.head is None:
            self.head = new_node

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insertion_into_the_kth(self, value, k):
        new_node = Node(value)
        if k < 0:
            print("Invalid Input")
            return

        if k == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        count = 0
        while current and count < k - 1:
            current = current.next
            count += 1

        if current is None:
            print("Position Out of range")
        else:
            new_node.next = current.next
            current.next = new_node


arr = [3, 4, 5, 7, 8, 100]
ll = LinkedList()

for data in arr:
    ll.append(data)

ll.display()
print(ll.length_of_an_array())

print(ll.check_value_in_ll(212))

# ll.delete(112)
# ll.display()

# ll.delete_tail_from_ll()
# ll.display()

# ll.delete_kth_element_from_ll(809)
# ll.display()

ll.insertion_into_the_kth(348, 6)
ll.display()
