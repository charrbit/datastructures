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
    
    def __getNodeAtIndex(self, index):
        # index out of range
        if index < 0 or index > self.length - 1: return
        # start at the beginning of the list
        current_index, current_node = 0, self.head
        while current_index < index:
            current_index += 1
            current_node = current_node.next
        return current_node
    
    def __insertAtIndex(self, node, index):
        # get the node before the desired index for O(n)
        # insertion anywhere other than the head and tail
        node_before = self.__getNodeAtIndex(index - 1)
        # insert at head, O(1)
        if index == 0:
            node.next = self.head
            # first node inserted
            if self.head == None:
                self.tail = node
            self.head = node
        # insert at tail, O(1)
        elif index == self.length:
            node_before = self.tail
            node.next = node_before.next
            node_before.next = node
            self.tail = node
        # insert somewhere in between, O(n)
        else:
            # if index is not out of range
            if node_before != None:
                node.next = node_before.next
                node_before.next = node
            else: return None, node_before
        self.length += 1
        return node, node_before
    
    def __removeAtIndex(self, index):
        # get the node before the desired index for O(n)
        # removal anywhere other than the head and tail
        node_before = self.__getNodeAtIndex(index - 1)
        # remove at head, O(1)
        if index == 0:
            node = self.head
            # node to remove is the only node in the list
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.head = node.next
        # remove at tail, O(1)
        elif index == self.length - 1:
            node = self.tail
            node_before.next = node.next
            self.tail = node_before
        # remove somewhere in between, O(n)
        else:
            # if index is not out of range
            if node_before != None and node_before != self.tail:
                node = node_before.next
                node_before.next = node.next
            else: return
        self.length -= 1
        return node
    