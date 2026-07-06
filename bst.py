class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    # INSERT
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

        elif data.kode > current.data.kode:
            if current.right is None:
                current.right = BSTNode(data)
            else:
                self._insert(current.right, data)

        else:
            print("Kode laundry sudah ada!")

    # SEARCH
    def search(self, kode):
        return self._search(self.root, kode)

    def _search(self, current, kode):
        if current is None:
            return None

        if kode == current.data.kode:
            return current.data

        elif kode < current.data.kode:
            return self._search(current.left, kode)

        else:
            return self._search(current.right, kode)

    # DELETE
    def delete(self, kode):
        self.root = self._delete(self.root, kode)

    def _delete(self, current, kode):
        if current is None:
            return current
        if kode < current.data.kode:
            current.left = self._delete(current.left, kode)
        elif kode > current.data.kode:
            current.right = self._delete(current.right, kode)
        else:
            # Tidak punya anak kiri
            if current.left is None:
                return current.right
            # Tidak punya anak kanan
            if current.right is None:
                return current.left
            # Dua anak
            temp = self._min_value(current.right)
            current.data = temp.data
            current.right = self._delete(current.right, temp.data.kode)

        return current

    def _min_value(self, node):
        current = node

        while current.left:
            current = current.left

        return current

    # INORDER
    def inorder(self):
        if self.root is None:
            print("\nData laundry kosong.")
        else:
            self._inorder(self.root)

    def _inorder(self, current):
        if current:
            self._inorder(current.left)
            print(current.data)
            print("-" * 40)
            self._inorder(current.right)

    # PREORDER
    def preorder(self):
        if self.root is None:
            print("\nData laundry kosong.")
        else:
            self._preorder(self.root)

    def _preorder(self, current):
        if current:
            print(current.data)
            print("-" * 40)
            self._preorder(current.left)
            self._preorder(current.right)

    # POSTORDER
    def postorder(self):
        if self.root is None:
            print("\nData laundry kosong.")
        else:
            self._postorder(self.root)

    def _postorder(self, current):
        if current:
            self._postorder(current.left)
            self._postorder(current.right)
            print(current.data)
            print("-" * 40)

    # HEIGHT
    def height(self):
        return self._height(self.root)

    def _height(self, current):
        if current is None:
            return 0

        kiri = self._height(current.left)
        kanan = self._height(current.right)

        return max(kiri, kanan) + 1

    # NODE COUNT
    def node_count(self):
        return self._node_count(self.root)

    def _node_count(self, current):
        if current is None:
            return 0

        return (
            1
            + self._node_count(current.left)
            + self._node_count(current.right)
        )

    # CEK KOSONG
    def is_empty(self):
        return self.root is None