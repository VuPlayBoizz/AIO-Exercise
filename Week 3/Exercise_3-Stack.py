class Stack():
    def __init__(self, capacity):
        self.capacity = capacity
        self.my_stack = []

    def is_empty(self):
        return len(self.my_stack) == 0

    def is_full(self):
        return len(self.my_stack) == self.capacity

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.my_stack.pop()

    def push(self, value):
        if self.is_full():
            return "Stack is full"
        return self.my_stack.append(value)

    def top(self):
        if self.is_empty():
            return "Stack is empty"
        return self.my_stack[-1]


stack1 = Stack(capacity=5)

stack1.push(1)
stack1.push(2)

print(stack1.is_full())

print(stack1.top())

print(stack1.pop())

print(stack1.top())

print(stack1.pop())

print(stack1.is_empty())
