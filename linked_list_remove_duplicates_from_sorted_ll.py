# You are given the pointer to the head node of a sorted linked list, where the data in the nodes is in ascending order. 
# Delete nodes and return a sorted list with each distinct value in the original list. 
# The given head pointer may be null indicating that the list is empty.
#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
def removeDuplicates(head):
    # move through list, comparing current to previous
        # if current is equal to previous, then this is a duplicate that we have to delete
            # link previous's next node to current's next node so the linkedlist stays intact
            # current node updates to the next node we just linked from previous
            # continue with loop to compare new current to previous
        # else current is greater than previous, keep moving through linked list
            # previous becomes the node we just looked at
            # current node moves on to the next node
    
    #return head