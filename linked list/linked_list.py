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
    def remove_at_index(self,index):
        previous=None
        current=self.head

        if index == 0:
            self.remove_at_begin()
        else:
            count=0
            while current.next is not None:
                if index==count:
                    next_node=current.next
                    current.next=None
                    previous.next=next_node
                    break

                count+=1
                previous=current
                current=current.next        
    def remove_at_end(self):
        if self.head is None:
            return None
        
        current=self.head
        previous=None

        while current.next is not None:
            previous=current
            current=current.next
        previous.next=None
        return current.data

    def remove_at_begin(self):
        if self.head is None:
            return None
        
        temp=self.head
        self.head=self.head.next
        return temp
    def concatenate(self,list):
        current=self.head
        if self.head is None:
            current.next=list.head
        else:
            while current.next is not None:
                current=current.next
            current.next=list.head            
    def invert(self):
        current=self.head
        previous= None
        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        self.head = previous
    def display(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next    