# Given the head of a singly linked list, return the middle node of the linked list.
# If there are two middle nodes, return the second middle node.
# Middle of the LL

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
        while current != None:
            print(current.data, end='->')
            current = current.next
        print('None')

    # Using Tortoise & Hare Algorithm
    # Take two pointers one slow and one fast pointer initially both pointing at head
    # if slow pointer moves one step, fats one moves twice as that that is 2 step
    # Tranverse in the ll until we get null
    # in odd number of nodes - the slow pointer points at the middle Node and the fast pointer points at the last node
    # in even number of nodes - the slow pointer points at the middle of the node and the fast pointer points at Null
    def findMiddleNode(self):
        slow_pointer = self.head
        fast_pointer = self.head
        while fast_pointer != None and fast_pointer.next != None:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
        self.head = slow_pointer
        return


head = [1, 2, 3, 4, 5, 6]
ll = LinkedList()

for data in head:
    ll.append(data)

ll.findMiddleNode()
ll.display()

# print(len(head)//2, head[len(head)//2:])
