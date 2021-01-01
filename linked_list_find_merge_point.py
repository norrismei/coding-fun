# Given pointers to the head nodes of 2 linked lists that merge together at some point, 
# find the node where the two lists merge. The merge point is where both lists point to the same node, 
# i.e. they reference the same memory location. It is guaranteed that the two head nodes will be different, 
# and neither will be NULL. If the lists share a common node, return that node's  value.

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        print(str(node.data))

        node = node.next

# Complete the findMergeNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def findMergeNode(head1, head2):
    # Create a set to keep track of all nodes that we've visited
    visited_nodes = set()
    # Starting at each head, traverse through lists simultaneously
    curr1 = head1
    curr2 = head2
    # While there are still nodes left in the first list or second list
    while curr1 or curr2:
        # check if the current node is in the set.
        # if yes, return the data of that node
        # if not, add the current node to the set and move to next
        if curr1 and curr1 in visited_nodes:
            return curr1.data
        elif curr1:
            visited_nodes.add(curr1)
            curr1 = curr1.next
        
        if curr2 and curr2 in visited_nodes:
            return curr2.data
        elif curr2:
            visited_nodes.add(curr2)
            curr2 = curr2.next
    
