class queue_with_stack:
    def __init__(self):
        self.enqueue_stack=[]
        self.dequeue_stack=[]
        
    def push(self,item):
        self.enqueue_stack.append(item)
    def pop(self):
        if len(self.dequeue_stack)==0:
            while len(self.enqueue_stack)==0:
                last=self.enqueue_stack[-1]
                del self.enqueue_stack[-1]
                self.dequeue_stack.append(last)
                #self.dequeue_stack.append(self.enqueue_stack[-1])
                del self.enqueue_stack[-1]

        if not len(self.dequeue_stack)==0:
            item=self.dequeue_stack[-1]
            del self.dequeue_stack[-1]
            return item
        else:
            raise Exception("queue is empty")