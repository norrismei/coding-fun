# You are given the pointer to the head node of a sorted linked list, where the data in the nodes is in ascending order. 
# Delete nodes and return a sorted list with each distinct value in the original list. 
# The given head pointer may be null indicating that the list is empty.
#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next

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

def print_singly_linked_list(node):
    while node:
        print(str(node.data))

        node = node.next

def removeDuplicates(head):
    # if linked list is empty, return None
    if head is None:
        return None
    
    # if linked list only has one node, then there are no duplicates to remove
    if head.next is None:
        return head
    else:
    # starting with first two nodes as prev and curr, move through list, comparing current to previous
        previous = head
        current = head.next
    
    while current:
        # if current is equal to previous, then this is a duplicate that we have to delete
        if current.data == previous.data:
            # link previous's next node to current's next node so the linkedlist stays intact
            previous.next = current.next
            # current node updates to the next node we just linked from previous
            current = current.next
            # continue with loop to compare new current to previous
            continue
        # else current is greater than previous, keep moving through linked list
        else:
            # previous becomes the node we just looked at
            previous = current
            # current node moves on to the next node
            current = current.next
    
    return head

ll = SinglyLinkedList()
for num in [1, 2, 2, 3, 3, 5]:
    ll.insert_node(num)

print_singly_linked_list(removeDuplicates(ll.head))

