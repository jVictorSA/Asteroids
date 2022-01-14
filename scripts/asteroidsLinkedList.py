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
        self.head = node

    #insert asteroid at the end of the list
    def insertBack(self, node):
        if self.head is None:
            self.head = node
        else:
            for actualNode in self:
                pass
        actualNode.next = node
    
    #insert a node ahead another node
    def insertBetween(self, previous,node):
        if previous.next == None:
            previous.next = node
        else:
            node.next = previous.next
            previous.next = node
            

    #delete a node 
    def deleteNode(self, node, previousNode = None):
        if previousNode == None:
            self.head = node.next
            del node
        else:
            previousNode.next = node.next
            del node
        

    #iterator for the class
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    #print every node of the list in order
    def printList(self):
        node = self.head
        while node != None:
            print(node.asteroid)
            node = node.next

#instance of the class
asteroidsLinkedList = linkedList()