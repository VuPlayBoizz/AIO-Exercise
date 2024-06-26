class Queue():
    def __init__(self, capacity):
        self.capacity = capacity
        self.my_queue = []

    def is_empty(self):
        return len(self.my_queue) == 0

    def is_full(self):
        return len(self.my_queue) == self.capacity

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        return self.my_queue.pop(0)

    def enqueue(self, value):
        if self.is_full():
            return "Queue is full"
        return self.my_queue.append(value)

    def front(self):
        if self.is_empty():
            return "Queue is empty"
        return self.my_queue[0]


queue1 = Queue(capacity=5)

queue1.enqueue(1)

queue1.enqueue(2)

print(queue1.is_full())

print(queue1.front())

print(queue1.dequeue())

print(queue1.front())

print(queue1.dequeue())

print(queue1.is_empty())
