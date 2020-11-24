class Stack:
    """Stack implementation as a list"""

    def __init__(self):
        """Create new stack"""
        self._items = []

    def is_empty(self):
        """Check if the stack is empty"""
        return not bool(self._items)

    def push(self, item):
        """Add an item to the stack"""
        self._items.append(item)

    def pop(self):
        """Remove an item from the stack"""
        if not self.is_empty():
            return self._items.pop()
        return "Cannot pop. Stack is empty."

    def peek(self):
        """Get the value of the top item in the stack"""
        if not self.is_empty():
            return self._items[-1]
        return "Nothing to peek. Stack is empty."

    def size(self):
        """Get the number of items in the stack"""
        return len(self._items)