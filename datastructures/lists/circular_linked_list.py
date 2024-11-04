from datastructures.lists.doubly_linked_list import DoublyLinkedList

# circular linked list

# assumes a list node structure of:
#   class node:
#       data: any python object
#       next: node
#       prev: node

class CircularLinkedList(DoublyLinkedList):
    def __init__(self):
        super().__init__()

    def insertAtIndex(self, node, index):
        node = super().insertAtIndex(node, index)
        if node != None:
            if node.next == None:
                node.next = node.prev = node
            elif node.prev == None:
                node.prev = self.tail
                self.tail.next = node
        return node
    
    def insertAtHead(self, node):
        return self.insertAtIndex(node, 0)
    
    def insertAtTail(self, node):
        return self.insertAtIndex(node, self.length)
    
    def removeAtIndex(self, index):
        node = super().removeAtIndex(index)
        if node != None:
            if node.prev != None:
                node.prev.next = node.next

    def removeAtHead(self):
        return self.removeAtIndex(0)

    def removeAtTail(self):
        return self.removeAtIndex(self.length - 1)