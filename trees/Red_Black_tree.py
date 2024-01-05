class Node:
    def __init__(self, key, color, parent, left, right):
        self.key = key
        self.color = color
        self.parent = parent
        self.left = left
        self.right = right

class RedBlackTree:
    def __init__(self):
        self.NIL = Node(None, "BLACK", None, None, None)
        self.root = self.NIL

    def insert(self, key):
        new_node = Node(key, "RED", None, self.NIL, self.NIL)
        self._insert(new_node)
        self._insert_fixup(new_node)

        self.root.color = "BLACK"

    def _insert(self, z):
        y = None
        x = self.root

        while x != self.NIL:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right

        z.parent = y
        if y is None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

    def _insert_fixup(self, z):
        while z.parent is not None and z.parent.color == "RED":
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y is not None and y.color == "RED":
                    z.parent.color = "BLACK"
                    y.color = "BLACK"
                    z.parent.parent.color = "RED"
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self._left_rotate(z)
                    if z.parent is not None:
                        z.parent.color = "BLACK"
                    if z.parent.parent is not None:
                        z.parent.parent.color = "RED"
                    if z.parent.parent is not None:
                        self._right_rotate(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y is not None and y.color == "RED":
                    z.parent.color = "BLACK"
                    y.color = "BLACK"
                    z.parent.parent.color = "RED"
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self._right_rotate(z)
                    if z.parent is not None:
                        z.parent.color = "BLACK"
                    if z.parent.parent is not None:
                        z.parent.parent.color = "RED"
                    if z.parent.parent is not None:
                        self._left_rotate(z.parent.parent)

        self.root.color = "BLACK"


    def _left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    def _right_rotate(self, y):
        x = y.left
        y.left = x.right
        if x.right != self.NIL:
            x.right.parent = y

        x.parent = y.parent
        if y.parent is None:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x

        x.right = y
        y.parent = x

    def remove(self, key):
        z = self._search(key)
        if z is not None:
            self._remove(z)

    def _search(self, key):
        current = self.root
        while current != self.NIL and current.key != key:
            if key < current.key:
                current = current.left
            else:
                current = current.right
        return current

    def _remove(self, z):
        y = z
        y_original_color = y.color

        if z.left == self.NIL:
            x = z.right
            self._transplant(z, z.right)
        elif z.right == self.NIL:
            x = z.left
            self._transplant(z, z.left)
        else:
            y = self._minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self._transplant(y, y.right)
                y.right = z.right
                y.right.parent = y

            self._transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color

        if y_original_color == "BLACK":
            self._remove_fixup(x)

    def _transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v

        v.parent = u.parent

    def _minimum(self, x):
        while x.left != self.NIL:
            x = x.left
        return x

    def _remove_fixup(self, x):
        while x != self.root and x.color == "BLACK":
            if x == x.parent.left:
                w = x.parent.right
                if w.color == "RED":
                    w.color = "BLACK"
                    x.parent.color = "RED"
                    self._left_rotate(x.parent)
                    w = x.parent.right

                if w.left.color == "BLACK" and w.right.color == "BLACK":
                    w.color = "RED"
                    x = x.parent
                else:
                    if w.right.color == "BLACK":
                        w.left.color = "BLACK"
                        w.color = "RED"
                        self._right_rotate(w)
                        w = x.parent.right

                    w.color = x.parent.color
                    x.parent.color = "BLACK"
                    w.right.color = "BLACK"
                    self._left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == "RED":
                    w.color = "BLACK"
                    x.parent.color = "RED"
                    self._right_rotate(x.parent)
                    w = x.parent.left

                if w.right.color == "BLACK" and w.left.color == "BLACK":
                    w.color = "RED"
                    x = x.parent
                else:
                    if w.left.color == "BLACK":
                        w.right.color = "BLACK"
                        w.color = "RED"
                        self._left_rotate(w)
                        w = x.parent.left

                    w.color = x.parent.color
                    x.parent.color = "BLACK"
                    w.left.color = "BLACK"
                    self._right_rotate(x.parent)
                    x = self.root

        x.color = "BLACK"

    def display(self):
        self._display(self.root, 0)

    def _display(self, node, level):
        if node != self.NIL:
            self._display(node.right, level + 1)
            print("   " * level + f"{node.key} ({node.color})")
            self._display(node.left, level + 1)


# Test :
tree = RedBlackTree()

# Insert :
tree.insert(20)
tree.insert(10)
tree.insert(25)
tree.insert(5)
tree.insert(18)
tree.insert(21)
tree.insert(35)


print("Original Red-Black Tree:")
tree.display()

# Remove
tree.remove(20)

# Display :
print("\nRed-Black Tree after removing 5:")
tree.display()

