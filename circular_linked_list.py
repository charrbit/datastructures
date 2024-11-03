from doubly_linked_list import DoublyLinkedList

# circular linked list

# assumes a list node structure of:
#   class node:
#       data: any python object
#       next: node
#       prev: node

class CircularLinkedList(DoublyLinkedList):
    def __init__(self):
        super().__init__()

    