class Queue():

    def __init__(self,max):
        self.max_size = max
        self.queue = [None] * self.max_size
        self.rear = self.front = -1

    def enqueue(self,item):

        if(self.rear == -1):
            self.rear += 1
            self.queue[self.rear] = item
        elif self.rear == self.max_size:
            self.Is_full()
        else:
            self.rear += 1
            self.queue[self.rear] = item


    def dequeue(self):
        if self.rear != -1:
            for i in range(self.max_size - 1):
                self.queue[i] = self.queue[i + 1]
        else:
            self.Is_empty()
    
    def Is_empty(self):
        if self.front == self.rear:
            return True
        else: False
        
    def Is_full(self):
        if self.rear == self.max_size-1:
            return True
        else: False
        
    def reverse_queue(self):
        for i in range(self.max_size+1,0,-1):
            return self.queue[i]


    
    def peek(self):
                
        return self.queue[self.front]

    def display(self):
        for i in self.queue:
            print(i)
        
        

        #test


queue1 = Queue(5)
queue1.enqueue(1)

queue1.enqueue(2)
queue1.enqueue(3)
queue1.dequeue()
#queue1.Is_empty()
queue1.display()
print(queue1.peek())
print(queue1.reverse_queue())

