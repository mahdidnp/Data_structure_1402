class Node():
    def __init__(self, val):
        self.right=None
        self.left=None
        self.value=val

class Binary_Tree(Node):

    def __init__(self):
        self.root=None

    def insert(self, value):

        if self.root == None:
            self.root=Node(value)

        else: 
            self._insert(value, self.root)

    def _insert(self, value, node):

        if node is None:
            return Node(value)
     
        elif value < node.value:
            node.left = self._insert(value, node.left)
            return node
        elif value > node.value:
            node.right = self._insert(value, node.right)
            return node
        else: 
            return node    
        

    def search(self, value):
        return self._search(value, self.root )
    def _search(self,value, node):
        current=self.root
        while current!=None:
            if value<current.value:
                current=current.left
            elif value>current.value:
                current=current.right
            else:
                return True
        return False
        # if node is None:
        #     return node
        # if node.value==value:
        #     return True
        # elif value < node.value:
        #     return self._search(value, node.right)
        # return self._search(value, node.left)

    
    def inorder_display(self):
        self.root =self._inorder_display(self.root)

    def _inorder_display(self, node):

        if node==None:
            return
        self._inorder_display(node.left)
        print(node.value)
        self._inorder_display(node.right)

    def postorder_display(self):
        self.root = self._postorder_display(self.root)

    def _postorder_display(self,node):
        if node==None:
            return
        self._postorder_display(node.left)
        self._postorder_display(node.right)
        print(node.value)

    def preorder_display(self):
        self.root=self._preorder_display(self.root)

    def _preorder_display(self,node):
        if node==None:
            return
        print(node.value)
        self._preorder_display(node.left)
        self._preorder_display(node.right)

    def min(self, root_value):
        self.node(root_value)
        return self._min(self.node(root_value))
        # return self._min(root_value)
    
    
    def _min(self, node):
        if node==None:
            return -1
        if node.left==None:
            return node.value
        else:
            return self._min(node.left)
        
    def parent(self , value):
        return self._parent(self.root, value, parent=None)
    
    def _parent(self, node, value, parent):

        if node is None:
            return node
 
        if node.value == value:
          return parent

        parent = self._parent(node.left, value, node.value)
        if parent is None:
            return self._parent(node.right, value, node.value)
        return parent
    
    def node(self, value):
        return self._node(value, self.root)
    def _node(self, value, node):
        if node==None:
            return 
        if node.value==value:
            return node
        
        return_node=self._node(value, node.left)
        if return_node is None:
            return self._node(value, node.right)
        return return_node

    def remove(self, value):

        node_of_value=self.node(value)
        if node_of_value.left is None and node_of_value is None:
            self.remove_nil(value) 

        elif node_of_value.left is not None or node_of_value.right is not None:
            self.remove_prent_nil(self, value)

        else:
            min=self.node(self.parent(self.min(node_of_value.right.value)))
            node_of_value.value=self.min(node_of_value.right.value)
            min.left=None

    def remove_nil(self, value):
        parent=self.parent(value)
        if value > parent.value:
            parent.right=None
        else:
            parent.left=None

    def remove_prent_nil(self, value):
        node_of_value=self.node(value)
        node_of_value.value=node_of_value.right.value
        node_of_value.right=None

    





    

                    








tree=Binary_Tree()
tree.insert(20)
tree.insert(22)
tree.insert(13)
tree.insert(8)
tree.insert(18)
tree.insert(15)
tree.insert(10)
tree.insert(19)
tree.insert(5)

# print(tree.search(30))
# print(tree.min(3))
# print(tree.parent(1))
tree.inorder_display()
tree.remove(5)
tree.inorder_display()

# tree.preorder_display()
# tree.postorder_display()
