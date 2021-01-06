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
    if not head1:
        return head2
    # if head2 is null, return head1
    elif not head2:
        return head1

    # Create a new linkedlist for our merged linked lists
    merged = SinglyLinkedList()

    # Current node will start at each respective head
    curr1 = head1
    curr2 = head2

    # while there are still nodes in list1 and list2, compare the data of the current nodes. 
    while curr1 and curr2:
        # if node in list1 is less than or equal to node in list2,
        if curr1.data <= curr2.data:
            # insert the node into the merged linked list
            merged.insert_node(curr1.data)
            # curr1 will move to its next node
            curr1 = curr1.next
        # else, the node in list1 is greater than the node in list2,
        else:
            # so insert the node in list2 to the merged linked list
            merged.insert_node(curr2.data)
            # curr2 will move to its next node
            curr2 = curr2.next

    # if curr1 is null, then we've gone through all of list1.
    if not curr1:
        # to add the rest of list2, insert curr2 node and move to next while there are still nodes in curr2
        while curr2:
            merged.insert_node(curr2.data)
            curr2 = curr2.next
    # else, if curr2 is null, then we've gone through all of list2.
    elif not curr2:
        # to add the rest of list1, insert curr1 node and move to next while there are still nodes in curr1
        while curr1:
            merged.insert_node(curr1.data)
            curr1 = curr1.next

    # return the head of the merged linked list
    return merged.head

