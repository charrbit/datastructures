from singly_linked_list import SinglyLinkedList

# doubly linked list

# assumes a list node structure of:
#   class node:
#       data: any python object
#       next: node
#       prev: node

class DoublyLinkedList(SinglyLinkedList):
    def __init__(self):
        super().__init__()

    