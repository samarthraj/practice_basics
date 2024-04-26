# Stacks - First In Last Out
class Stacks:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        if len(self.stack) == 0:
            return

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from an empty stack")
        # pops the first element or element on top of the stack.
        return self.stack.pop()

    def peek(self):
        # this one does not remove the element from the stack but returns what element is present
        if self.is_empty():
            raise IndexError("peek from an empty stack")
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def display_element_of_stack(self):
        for element in self.stack:
            print(element, end=' ')


my_stack = Stacks()

my_stack.push(10)
my_stack.push(20)
my_stack.push(30)

my_stack.display_element_of_stack()
print(" Stack size:", my_stack.size())
print("Top element:", my_stack.peek())

popped_element = my_stack.pop()
print("Popped element:", popped_element)
my_stack.display_element_of_stack()
print("Top element:", my_stack.peek())
