class Queue:
    front =rear=-1

    def __init__(self,size) :
        self.size=size
        self.queue = [None]*size

