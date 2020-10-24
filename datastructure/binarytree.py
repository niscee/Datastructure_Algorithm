class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


    def insert(self, val):
        current = self.value

        if current > val:
            if self.left is None:
                self.left = BinaryTree(val)
            else:
                self.left.insert(val)

        elif current < val:
            if self.right is None:
                self.right = BinaryTree(val)
            else:
                self.right.insert(val)

        else:
            self.value = val



    def printTree(self):
        if self.left:
            self.left.printTree()
        
        print(self.value)

        if self.right:
            self.right.printTree()                    


# initializing BinaryTree object.
treeobj = BinaryTree(12)
treeobj.insert(6)
treeobj.insert(5)
treeobj.insert(9)
treeobj.insert(14)
treeobj.insert(13)
treeobj.insert(18)
treeobj.printTree()    