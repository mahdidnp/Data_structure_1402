import linked_list
class queue():

    queue=linked_list.linked_list()
    
    def push(self,data):
        self.queue.insert_at_end(data)

    def pop(self):
        self.queue.remove_at_begin()
    
    def display(self):
        self.queue.display()

