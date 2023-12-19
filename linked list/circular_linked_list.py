class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
class curcular_linked_list:
    def __init__(self):
        self.head=None
        self.last=None

    def insert_at_end(self,data):

        new_node=Node(data)        
        if self.last is None:

            self.head=new_node
            self.last=new_node
            new_node.next = self.head

        else:

            self.last.next=new_node
            new_node.next=self.head
            self.last=new_node
        
    def insert_at_begin(self,data):
        new_node=Node(data)
        last= self.last

        last.next=new_node
        new_node.next=self.head
        self.head=new_node

    def insert_at_index(self, value , index):
        new_node=Node(value)

        if index<0 or index>=self.size_of_list():
            raise Exception("Binamos Dalgak")

        if index==0:

            if self.head is None:
                self.head = new_node
                self.last = new_node
                new_node.next = self.head
            else:
                new_node.next = self.head
                self.last.next = new_node
                self.head = new_node
            return

        current=self.head
        for _ in range(index-1):
            current=current.next
        new_node.next = current.next
        current.next = new_node

    def size_of_list(self):
        current=self.head
        count=0
        while current.next != self.head:
            count+=1
            current=current.next
        return count+1
    
    def update_node(self,value,index):
        current=self.head

        if index==0:
            self.head.data=value

        count=0
        while current.next != self.head:
            if index==count:
                current.data=value
                break
            count+=1
            current=current.next

    def remove_at_end(self):
        if self.last is None:
            return None
        
        current=self.head
        previous=None

        while current.next != self.head:
            previous=current
            current=current.next
        previous.next=self.head
        self.last=previous
        return current.data
    
    def remove_at_begin(self):
        self.last.next=self.head.next
        self.last=self.head.next
        self.head=self.head.next

    def concatenate(self, list):
        if self.last is None:
            self.head.next=list.head
            self.last=list.last
        else:
            self.last.next=list.head
            list.last=self.head
            self.last=list.last

    def remove_at_index(self, index):

        if index<0 or index>self.size_of_list():
            raise Exception("Binamose Dalgak")
        
        elif index==0:
                self.last=self.head.next
                self.last=self.head.next
                self.head=self.head.next
        else:
            current=self.head
            previous=None
            count=0
            while current.next != self.head:
                if count==index:
                    next_node=current.next
                    current.next=None
                    previous.next=next_node
                    break

                count+=1
                previous=current
                current=current.next

    def invert(self):
        previous=self.last
        current=self.head
        while True:
            temp=current.next
            current.next=previous
            previous=current
            current=temp

            if current==self.head:
                break
        
        self.last=previous
        self.head=previous

    def size_of_list(self):
        count=0
        current=self.head
        while current.next is not None:
            count+=1
            current=current.next
        return count+1

    def display(self):
        current = self.head
        while current.next is not None:
            print(current.data)
            current = current.next
        print(current.data)

#TEST

obj=curcular_linked_list()
obj.insert_at_end(1)
obj.insert_at_end(2)
obj.insert_at_end(3)
obj.insert_at_end(4)
obj.insert_at_end(5)
obj.insert_at_end(6)
obj.insert_at_end(7)

# obj.insert_at_begin(88)
# obj.insert_at_index(48,5)
print(obj.size_of_list())
# obj.update_node(100,1)
# obj.remove_at_end()
# obj.remove_at_begin()
# obj.remove_at_index(2)
# obj.invert()

obj.display()