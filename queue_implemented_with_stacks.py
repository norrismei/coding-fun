class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = Stack() # 2, 1
        self.waiting_stack = Stack()
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        while not self.queue.is_empty():
            front_num = self.queue.pop()
            self.waiting_stack.push(front_num)
        
        self.queue.push(x)
        
        while not self.waiting_stack.is_empty():
            back_num = self.waiting_stack.pop()
            self.queue.push(back_num)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.queue.pop()
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.queue._items[-1]
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.queue._items

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
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()