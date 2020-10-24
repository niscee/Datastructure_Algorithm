""" linked list datastructure """ 

#creating node
class Node:
    def __init__(self, dataval=None):
        self.next = None
        self.dataval = dataval



#creating link-list
class LinkedList:
    def __init__(self):
        self.head = None
    
    #listing out all node.
    def printList(self):
        current = self.head
        while current:
            print(current.dataval)
            current = current.next
    
    #inserting new node to specific index.
    def addNewNode(self, index, dataval):
        current = self.head
        newNode = Node(dataval)
        counter = 0
        while current:
            counter += 1
            if counter == index - 1:
                if current.next:
                    newNode.next = current.next
                    current.next = newNode 
                else:
                    current.next = newNode    
            current = current.next

    #removing specific node.
    def removeNode(self, key):
        current = self.head
        counter = 0
        while current:
            counter += 1
            if counter == key - 1:
                delNode = current.next
                if delNode.next:
                   current.next = delNode.next
                else:   
                   current.next = None  
            current = current.next    
                       
    
    
    # reverse linklist
    def reversePrint(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev



            



#declaring node
node1 = Node("sunday")
node2 = Node("monday")
node4 = Node("wednesday")

#assigning head node
link_head = LinkedList()
link_head.head = node1
node1.next = node2
node2.next = node4

#listing out link-list.
print("-----------------------------")
link_head.printList()


#inserting new node.
print("-----------------------------")
print("After adding new node:")
link_head.addNewNode(3, "tuesday")
link_head.addNewNode(5, "thursday") 
link_head.printList()

print("-- reverse --")
link_head.reversePrint()
link_head.printList()


#remove existing node.
# print("-----------------------------")
# print("After removing node:")
# link_head.removeNode(5) 
# link_head.removeNode(2) 
# link_head.printList()

