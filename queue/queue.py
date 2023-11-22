class Queue:
    front =rear=-1

    def __init__(self,size) :
        self.size=size
        self.queue = [None]*size

    def enqueue(self, item):
        if self.rear==self.size:
            self.is_full()
        self.rear+=1
        self.queue[self.rear]=item

    def peek(self):
        return self.queue[self.front+1]
    
    def is_full(self):
        if self.rear==self.size:
            return True
        else:
            return False