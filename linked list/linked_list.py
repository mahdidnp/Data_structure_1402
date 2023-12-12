class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
class linked_list:
    def __init__(self):
        self.head=None

    def insert_at_end(self,data):

        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        
        else:
            current=self.head
            while current.next is not None:
                current=current.next
            current.next = new_node

    def insert_at_begin(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            new_node.next=self.head
            self.head=new_node

    def insert_at_index(self, value , index):
        new_node=Node(value)
        current=self.head

        if index<0 or index>=self.size_of_list():
            raise Exception("Binamos Dalgak")

        if index==0:
            new_node.next=self.head
            self.head=new_node

        for _ in range(index - 1):
            current=current.next
        new_node.next = current.next
        current.next = new_node

    def size_of_list(self):
        count=0
        current=self.head
        while current.next is not None:
            count+=1
            current=current.next
        return count+1
    
    def update_node(self,value,index):
        current=self.head

        if index==0:
            self.head.data=value

        count=0
        while current.next is not None:
            if index==count:
                current.data=value
                break
            count+=1
            current=current.next