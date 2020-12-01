class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """

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