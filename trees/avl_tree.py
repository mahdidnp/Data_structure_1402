
class AVLNode:
    def __init__(self, value):
        self.value = value
        self.RightChilde = None
        self.LeftChilde = None
        self.height = 1
        

class AVLTree:

    def insert(self, root, value):

        if not root :
            return AVLNode(value)
        elif value < root.value:
            root.LeftChilde = self.insert(root.LeftChilde, value)
        else:
            root.RightChilde = self.insert(root.RightChilde, value)

        root.height = 1 + max(self.getHeight(root.LeftChilde), self.getHeight(root.RightChilde))

        BalanceFactor = self.GetBalance(root)
        if BalanceFactor > 1:
            if value < root.LeftChilde.value:
                self.RightRotate(root)
            else:
                root.LeftChilde = self.LeftRotate(root.LeftChilde)
                self.RightRotate(root)
        if BalanceFactor < -1:
            if value > root.RightChilde.value:
                return self.LeftRotate(root)
            else:
                root.RightChilde = self.RightRotate(root.RightChilde)
                return self.LeftRotate(root)
        return root
    
    def Remove(self, root, value):
        if not root:
            return root
        elif value < root.value:
            root.LeftChilde = self.Remove(root.LeftChilde, value)
        elif value > root.value:
            root.RightChilde = self.Remove(root.RightChilde, value)
        else:
            if root.LeftChilde is None:
                temp = root.RightChilde
                root = None
                return temp
            elif root.RightChilde is None:
                temp = root.LeftChilde
                root = None
                return temp
            temp = self.GetMinValueNode(root.RightChilde)
            root.value = temp.value
            root.RightChilde = self.Remove(root.RightChilde, temp.value)

        if root is None:
            return root    
        
        root.height = 1 + max(self.getHeight(root.LeftChilde), 
                              self.getHeight(root.RightChilde))

        BalanceFactor = self.GetBalance(root)

        if BalanceFactor >  1:
            if self.GetBalance(root.LeftChilde) >= 0:
                return self.RightRotate(root)
            else:
                root.LeftChilde = self.LeftRotate(root.LeftChilde)
                return self.LeftRotate(root)
        if BalanceFactor < -1:
            if self.GetBalance(root.RightChilde) <= 0:
                return self.LeftRotate(root)
            else:
                root.RightChilde = self.RightRotate(root.height)
                return self.LeftRotate(root)
            self.left
        return root      


    def getHeight(self, root):
        if not root:
            return 0 
        return root.height
    
    def GetBalance(self, root):
        if root == None:
            return 0
        return self.getHeight(root.LeftChilde) - self.getHeight(root.RightChilde)
    
    def RightRotate(self, z):
        y = z.LeftChilde
        T3 = y.RightChilde
        y.RightChilde = z
        z.LeftChilde = T3
        z.height = 1 + max(self.getHeight(z.LeftChilde), self.getHeight(z.RightChilde))
        y.height = 1 + max(self.getHeight(y.LeftChilde), self.getHeight(y.RightChilde))
        return y 
    
    def LeftRotate(self, z):
        y = z.RightChilde
        T2 = y.LeftChilde
        y.LeftChilde = z 
        z.RightChilde = T2
        z.height = 1 + max(self.getHeight(z.LeftChilde), self.getHeight(z.RightChilde))
        z.height = 1 + max(self.getHeight(y.LeftChilde), self.getHeight(y.RightChilde))
        return y 

    def GetMinValueNode(self, root):
        if root == None or root.LeftChilde == None:
            return root
        return self.GetMinValueNode(root.LeftChilde)