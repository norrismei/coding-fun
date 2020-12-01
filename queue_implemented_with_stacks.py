class Queue:

    def __init__(self):
        self._s1 = Stack()
        self._s2 = Stack()
    
    def enqueue(self, item):
        self._s1.push(item)
    
    # def dequeue(self):

    #     if not self._s2.is_empty():
    #         return self._s2.pop()
    #     elif self._s1.is_empty():
    #         return "There's nothing to dequeue"
    #     else:
    #         while not self._s1.is_empty():
    #             item = self._s1.pop()
    #             # print(f"item: {item}")
    #             self._s2.push(item)
        
    #         return self._s2.pop()
    
    def dequeue(self):
        # The queue is completely empty
        if self._s1.is_empty() and self._s2.is_empty():
            raise ValueError('Queue is empty.')
        
        if self._s2.is_empty():
            # Do transfer
            while not self._s1.is_empty():
                self._s2.push(self._s1.pop())

        return self._s2.pop()
    
    def size(self):
        return len(self._s1._items) + len(self._s2._items)
    
    def is_empty(self):
        return self._s1.is_empty() and self._s2.is_empty()

class Stack:
    
    def __init__(self):
        self._items = []
    
    def push(self, item):
        self._items.append(item)
    
    def peek(self):
        return self._items[-1]
    
    def pop(self):
        return self._items.pop()
    
    def size(self):
        return len(self._items)
    
    def is_empty(self):
        return not self._items

q = Queue()

for i in range(5):
    q.enqueue(i)

print('Dequeue: ', q.dequeue())
print('Dequeue: ', q.dequeue())
print('Dequeue: ', q.dequeue())
print('Dequeue: ', q.dequeue())
print('Dequeue: ', q.dequeue())
print('Empty:', q.is_empty() )