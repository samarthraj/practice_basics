# Queues Implementation using arrays
class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        len(self.queue) == 0
        return

    def enqueue(self, data):
        # adding elements in the queue, FIFO
        return self.queue.append(data)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from an empty queue")
        else:
            return self.queue.pop(0)

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from an empty queue")
        return self.queue[0]

    def size(self):
        return len(self.queue)

    def display_queue(self):
        for i in self.queue:
            print(i, end=' ')


my_queue = Queue()

# Enqueue elements into the queue
my_queue.enqueue(10)
my_queue.enqueue(20)
my_queue.enqueue(30)

my_queue.display_queue()
print("Queue size:", my_queue.size())
print("Front element:", my_queue.peek())

dequeued_element = my_queue.dequeue()
print("Dequeued element:", dequeued_element)
my_queue.display_queue()
