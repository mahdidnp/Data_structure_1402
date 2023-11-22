class stack():

    def __init__(self):
        self.stack=[]
    def pop(self):
        if not self.is_empty():   
            item=self.stack[-1]
            del self.stack[-1]
            return item
    def is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False