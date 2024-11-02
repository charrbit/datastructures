# base linked list to derive subclasses from

# assumes a list node structure of:
#   class node:
#       data: any python object
#       next: node

# utilizes a head "pointer" to track the beginning of the list, a tail "pointer" for subclass
# code reusability and, a length for performance benefits during insertion and deletion

class BaseLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __len__(self):
        return self.length