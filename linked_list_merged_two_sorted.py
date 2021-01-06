# Given pointers to the heads of two sorted linked lists, merge them into a single, sorted linked list. 
# Either head pointer may be null meaning that the corresponding list is empty.

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

def mergeLists(head1, head2):
# if head1 is null, return head2
# if head2 is null, return head1

# Create a new linkedlist for our merged linked lists
# Current node will start at each respective head

# while there are still nodes in list1 and list2, compare the data of the current nodes. 
    # if node in list1 is less than or equal to node in list2,
        # insert the node into the merged linked list
        # curr1 will move to its next node
    # else, the node in list1 is greater than the node in list2,
        # so insert the node in list2 to the merged linked list
        # curr2 will move to its next node

# if curr1 is null, then we've gone through all of list1.
    # to add the rest of list2, insert curr2 node and move to next while there are still nodes in curr2
# else, if curr2 is null, then we've gone through all of list2.
    # to add the rest of list1, insert curr1 node and move to next while there are still nodes in curr1

# return the head of the merged linked list

