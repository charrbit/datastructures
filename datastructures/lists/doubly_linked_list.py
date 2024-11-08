from datastructures.lists.singly_linked_list import SinglyLinkedList

# doubly linked list

# assumes a list node structure of:
#   class node:
#       data: any python object
#       next: node
#       prev: node

class DoublyLinkedList(SinglyLinkedList):
    def __init__(self):
        super().__init__()

    def insertAtIndex(self, node, index):
        node, nodeBefore = super().insertAtIndex(node, index)
        if node != None:
            if node.next != None:
                node.next.prev = node
            node.prev = nodeBefore
        return node

    def insertAtHead(self, node):
        return self.insertAtIndex(node, 0)
    
    def insertAtTail(self, node):
        return self.insertAtIndex(node, self.length)

    def removeAtIndex(self, index):
        node = super().removeAtIndex(index)
        if node != None:
            if node.next != None:
                node.next.prev = node.prev
        return node

    def removeAtHead(self):
        return self.removeAtIndex(0)
    
    def removeAtTail(self):
        return self.removeAtIndex(self.length - 1)
