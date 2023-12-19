class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.previouse=None
    
class double_linked_list:
    def __init__(self):
        self.head=None
        self.last=None

    def insert_at_end(self,data):
        new_node=Node(data)

        if self.head is None:
            self.head=new_node
        else:

            current=self.head
            while current.next is not None:
                current=current.next
            current.next=new_node
            new_node.previouse=current
            current=new_node

    def insert_at_begin(self,data):
        new_node=Node(data)

        if self.head is None:
            self.head=new_node

        new_node.next=self.head
        self.head.previouse=new_node
        self.head=new_node

    def insert_at_index(self, value, index):
        new_node=Node(value)

        if index<0 or index>=self.size_of_list():
            raise Exception("Binamos Dalgak")
        
        elif index==0:
            new_node.next=self.head
            self.head.previouse=new_node
            self.head=new_node
        else:
            current=self.head
            for _ in range(index):
                previous=current
                current=current.next
            
            current.previouse=new_node
            new_node.next=current
            new_node.previouse=previous
            previous.next=new_node
            current=new_node

    def remove_at_end(self):
        if self.head is None:
            raise Exception("list is empty")
        
        current= self.head
        previous=None
        while current.next is not None:
            previous=current
            current=current.next
        
        previous.next=None

    def remove_at_begin(self):
        if self.head is None:
            raise Exception("list is empty")
        
        temp=self.head.data
        current=self.head
        self.head=current.next

        if self.head is not None:
            current.previouse = None
        
        return temp
    
    def remove_at_index(self,index):
        if index<0 or index>=self.size_of_list():
            raise Exception("list is empty")
        
        elif index==0:
            self.remove_at_begin()
        
        current=self.head
        for _ in range(index):
            current=current.next
        
        current.previouse.next=current.next
        current.next.previouse=current.previouse
        
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

    def concatenate(self,list):
        current=self.head
        if self.head is None:
            current.next=list.head
            list.previouse=self.head
        else:
            while current.next is not None:
                current=current.next
            current.next=list.head 
            list.head.previoise=current

    def invert(self):
        current=self.head

        while current.next is not None:
            current.previouse, current.next = current.next, current.previouse
            current=current.previouse

        self.head=current.previouse

    def display(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next  

obj=double_linked_list()
obj.insert_at_end(1)
obj.insert_at_end(2)
obj.insert_at_end(3)
obj.insert_at_end(4)
obj.insert_at_end(5)
obj.insert_at_end(6)
obj.insert_at_end(7)

# obj.insert_at_begin(88)
# obj.insert_at_index(48,6)
# print(obj.size_of_list())
# obj.update_node(100,1)
# obj.remove_at_end()
# obj.remove_at_begin()
# obj.remove_at_index(2)
obj.invert()

obj.display()