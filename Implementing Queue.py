class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def show(self):
        print(self.items)

q = Queue()
print(q.is_empty())
q.enqueue(4)
q.enqueue('dog')
q.enqueue(True)
q.show()
print(q.size())
print(q.is_empty())
q.enqueue(8.4)
q.dequeue()
q.dequeue()
print(q.size())
q.show()