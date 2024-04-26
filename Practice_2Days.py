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


# first we define a class node which only has node and next in it
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
        ct = 0
        while current:
            print(current.data, end='->')
            ct = ct + 1
            current = current.next
        print('None')
        # print('Count: ' + str(ct))

    def check_if_present(self, val):
        current = self.head
        while current:
            if current.data == val:
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

    def delete_kth_element(self, k):
        if self.head is None or k < 0:
            return

        if k == 0:  # i.e. to delete the first element
            self.head = self.head.next
            return

        # current = self.head
        # prev = None
        # ct = 0
        # while current and ct < k:
        #     ct += 1
        #     prev = current
        #     current = current.next

        # if current is None:
        #     return

        # prev.next = current.next

        current = self.head
        ct = 0
        while current and ct < k - 1:
            ct += 1
            current = current.next

        if current is None or current.next is None:
            return

        current.next = current.next.next

    def delete_from_tail(self):
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

    def insert_into_head(self, insert_head):
        new_node = Node(insert_head)
        new_node.next = self.head
        self.head = new_node

    def insert_into_tail(self, insert_tail):
        new_node = Node(insert_tail)
        if self.head is None:
            self.head = new_node

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        return

    def insert_into_kth(self, k, k_data):
        new_node = Node(k_data)
        if k < 0:
            print("Invalid Input")
            return

        if k == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        ct = 0
        while current and ct < k - 1:
            ct += 1
            current = current.next

        if current is None:
            print("invalid")
        else:
            new_node.next = current.next
            current.next = new_node
        return


arr = [2, 4, 3, 1]
ll = LinkedList()

for data in arr:
    ll.append(data)

ll.display()

# print(ll.check_if_present(30))

# ll.delete_kth_element(3)
# ll.display()

# ll.delete_from_tail()
# ll.display()

ll.insert_into_kth(2, 7)
ll.display()
