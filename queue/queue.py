class Queue:
    front =rear=-1

    def __init__(self,size) :
        self.size=size
        self.queue = [None]*size

    def dequeue(self):
        if self.rear==self.front:
            self.is_empty()
        for i in range(self.size - 1):
            self.queue[i] = self.queue[i + 1]

    def peek(self):
        return self.queue[self.front+1]
    
    def reverse_queue(self):
        for i in range(self.size - 1, -1, -1):
            reversed_queue=self.queue[i]
        return reversed_queue
