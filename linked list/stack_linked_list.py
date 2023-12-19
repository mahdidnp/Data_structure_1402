import linked_list

class Stack():
    stack=linked_list.linked_list()

    def push(self,data):
        self.stack.insert_at_end(data)

    def pop(self):
        self.stack.remove_at_end()
    
    def display(self):
        self.stack.display()