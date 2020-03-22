class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self, item):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def peek(self):
        return self.items[len(self.items) -1]

    def size(self):
        return len(self.items)

    def show_stack(self):
        for item in reversed(self.items):
            print(item)

stack = Stack()
stack.push(1)
stack.push(5)
stack.push("s")
stack.push("sas")
stack.push(9)
stack.pop(5)
stack.push("rko")
stack.peek()
stack.push("123456789")
print("size: ", stack.size())
stack.show_stack()