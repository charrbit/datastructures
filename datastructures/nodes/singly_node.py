from datastructures.nodes.base_node import BaseNode

# singly linked list node with one
# "pointer" to the next node in the list

class SinglyNode(BaseNode):
    def __init__(self, data = None):
        super().__init__(data)
        self.next = None
