from datastructures.nodes.singly_node import SinglyNode

# doubly linked list node with two "pointers" 
# to the next and previous nodes in the list

class DoublyNode(SinglyNode):
    def __init__(self, data = None):
        super().__init__(data)
        self.prev = None