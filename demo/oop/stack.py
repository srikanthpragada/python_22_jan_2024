class Stack:
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        if self.length() == 0:   # stack is empty
            raise ValueError('Stack is empty!')

        return self.data.pop()

    @property   # getter
    def length(self):
        return len(self.data)

    def peek(self):
        return self.data[-1]  # take value at the top

    def clear(self):
        self.data.clear()


s = Stack()
s.push(10)
s.push(20)
print(s.peek())
print(s.length)  # Property
print(s.pop())
print(s.length)
