# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # Create dictionary where node is key, pos is value
        nodes = {}
        pos = 0
        curr = head
        
        # Traverse the linked list and add nodes and pos into the dictionary
        while curr is not None:
            if curr in nodes:
                return True
            else:
                nodes[curr] = [pos]
                pos += 1
                curr = curr.next
        
        # If made it to the end of the list, then there is no cycle
        return False