""" implementation of queue """ 



class Queue:

    def  __init__(self):
        self.queue = []


    def enqueue(self, val):
        if len(self.queue) == 0:
            self.queue.append(val)
        else:
            self.queue.insert(0, val)

    
    def isEmpty(self):
        return self.queue == []


    def dequeue(self):
        return self.queue.pop()

    
        

        

                     
