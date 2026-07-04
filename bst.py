class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
    if self.root is None:
        self.root = BSTNode(data)
    else:
        self._insert(self.root, data)

    def _insert(self, current, data):
        if data.kode < current.data.kode:
            if current.left is None:
                current.left = BSTNode(data)
            else:
                self._insert(current.left, data)
        else:
            if current.right is None:
                current.right = BSTNode(data)
            else:
                self._insert(current.right, data)
        
    def search(self, kode):
        return self._search(self.root, kode)

    def _search(self, current, kode):
        if current is None:
            return None

        if current.data.kode == kode:
            return current.data

        if kode < current.data.kode:
            return self._search(current.left, kode)

        return self._search(current.right, kode)    
    
    def inorder(self):
        self._inorder(self.root)

    def _inorder(self, current):
        if current:
            self._inorder(current.left)
            print(current.data)
            print("-" * 35)
            self._inorder(current.right)