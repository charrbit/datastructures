from base_linked_list import BaseLinkedList

# singly linked list derived from BaseLinkedList

# assumes a list node structure of:
#   class node:
#       data: any python object
#       next: node

class SinglyLinkedList(BaseLinkedList):
    def __init__(self):
        super().__init__()

    def insertAtIndex(self, node, index):
        return self._BaseLinkedList__insertAtIndex(node, index)
    
    def insertAtHead(self, node):
        return self.insertAtIndex(node, 0)
    
    def insertAtTail(self, node):
        return self.insertAtIndex(node, self.length)
    
    def removeAtIndex(self, index):
        return self._BaseLinkedList__removeAtIndex(index)
    
    def removeAtHead(self):
        return self.removeAtIndex(0)
        
    def removeAtTail(self):
        return self.removeAtIndex(self.length - 1)
