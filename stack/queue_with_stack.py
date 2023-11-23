class queue_with_stack:
    def __init__(self):
        self.enqueue_stack=[]
        self.dequeue_stack=[]
        
    def push(self,item):
        self.enqueue_stack.append(item)