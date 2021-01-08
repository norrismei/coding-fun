# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
         # base case: if either list becomes empty, return the other listNode
        if not l1:
            return l2
        elif not l2:
            return l1
        
        # compare l1 and l2 nodes. Return the smaller node but not before making recursive call using next of smaller node
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2