# base linked list node to derive subclasses from

class BaseNode:
    # data can be any python object
    def __init__(self, data = None):
        self.data = data
