import linked_list

class Array():

    array=linked_list.linked_list()

    def insert(self,value,data):
        self.array.insert_at_index(value,data)

    def remove(self,index):
        self.array.remove_at_index(index)
