#!/bin/python3

import math
import os
import random
import re
import sys

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
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the insertNodeAtPosition function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtPosition(head, data, position):

    if not head:
        return None
    
    # Find the position
    curr_position = 0
    previous = None
    curr = head
    
    while curr_position != position:
        previous = curr
        curr = curr.next
        curr_position += 1
    
    # When we're at the right position, create the node to be inserted.
    node = SinglyLinkedListNode(data)
    node.next = curr
    previous.next = node
    
    return head
    

if __name__ == '__main__':