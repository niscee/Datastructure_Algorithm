""" Stack datastructure """

class Stack:
    def __init__(self):
        self.stack = []

    def insert(self, value):
        if value not in self.stack:
            self.stack.append(value)
            return 0
        else:
            return 0

    def top(self):
        stack_len = len(self.stack)
        print(self.stack[stack_len-1])


    def listStack(self):
        for i in self.stack[::-1]:
            print(i)

    def remove(self):
        self.stack.pop()        


#create stack object
obj1 = Stack()
obj1.insert("sunday")
obj1.insert("monday")
obj1.insert("tuesday")
obj1.listStack()
obj1.remove()
print("---------After removing-----------")
obj1.listStack()


                



