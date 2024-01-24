class CircularQueue:
    def __init__(self, max_length):
        self.queue = {}
        self.max_length = max_length
        self.front = 0
        self.rear = 0

    def enqueue(self, element):
        if (self.rear + 1) % self.max_length == self.front:
            # Queue is full, dequeue the oldest element
            self.dequeue()

        # Add the new element to the queue
        self.queue[self.rear] = element
        self.rear = (self.rear + 1) % self.max_length

    def dequeue(self):
        if self.front == self.rear:
            # Queue is empty
            print("Queue is empty. Cannot dequeue.")
            return None

        # Dequeue the oldest element
        dequeued_element = self.queue[self.front]
        del self.queue[self.front]
        self.front = (self.front + 1) % self.max_length
        return dequeued_element

    def display(self):
        if self.front == self.rear:
            print("Queue is empty.")
            return

        print("Circular Queue:")
        current = self.front
        while current != self.rear:
            print(self.queue[current], end=" ")
            current = (current + 1) % self.max_length
        print()
