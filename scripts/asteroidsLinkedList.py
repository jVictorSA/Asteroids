class Node:
    #initialize node
    def __init__(self, asteroid=None):
        if asteroid is not None:
            self.asteroid = asteroid
        self.next = None

class linkedList:
    #initialize linked list
    def __init__(self):
        self.head = None

    #insert asteroid at the beggining of the list
    def insertFront(self, node):
        node.next = self.head
        self.head = Node(node)

    #insert asteroid at the end of the list
    def insertBack(self, node):
        if self.head is None:
            self.head = node
        else:
            for actualNode in self:
                pass
        actualNode.next = node
    
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def printList(self):
        for node in self:
            print(node.asteroid)

asteroidsLinkedList = linkedList()