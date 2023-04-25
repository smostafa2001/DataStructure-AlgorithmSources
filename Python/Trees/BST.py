class Node:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None   
        
class BST:
    def __init__(self, key=None):
        if key is None: self.root = None
        else: self.root = Node(key)
    def insert(self, key):
        self.root = self.__insert(self.root, key)
    def preorder(self):
        self.__preorder(self.root)
    def inorder(self):
        self.__inorder(self.root)
    def postorder(self):
        self.__postorder(self.root)
    def search(self, key):
        return self.__search(self.root, key)
    def deleteKey(self, key):
        self.root = self.__deleteKey(self.root, key)
    def minValue(self):
        return self.__minValue(self.root)
    def maxValue(self):
        return self.__maxValue(self.root)
    def lastCommonAncestor(self, x, y):
        self.__lastCommonAncestor(self.root, x, y)
    
    def __insert(self, root, key):
        if root is None:
            root = Node(key)
            return root
        elif key < root.key: root.left = self.__insert(root.left, key)
        elif key > root.key: root.right = self.__insert(root.right, key)
        return root
    def __preorder(self, root):
        if root is not None:
            print(root.key, end=" ")
            self.__preorder(root.left)
            self.__preorder(root.right)
    def __inorder(self, root):
        if root is not None:
            self.__inorder(root.left)
            print(root.key, end=" ")
            self.__inorder(root.right)
    def __postorder(self, root):
        if root is not None:
            self.__postorder(root.left)
            self.__postorder(root.right)
            print(root.key, end=" ")
    def __search(self, root, key):
        if root is None or root.key == key: return root
        if root.key < key: return self.__search(root.right, key)
        return self.__search(root.left, key)
    def __deleteKey(self, root, key):
        if root is None: return root
        if key < root.key: root.left = self.__deleteKey(root.left, key)
        elif key > root.key: root.right = self.__deleteKey(root.right, key)
        else:
            if root.left is None: return root.right
            elif root.right is None: return root.left
            root.key = self.__minValue(root.right)
            root.right = self.__deleteKey(root.right, root.key)
        return root
    def __minValue(self, root):
        minVal = root.key
        while root.left is not None:
            minVal = root.left.key
            root = root.left
        return minVal
    def __maxValue(self, root):
        maxVal = root.key
        while root.right is not None:
            maxVal = root.right.key
            root = root.right
        return maxVal
    def __lastCommonAncestor(self, root, x, y):
        if root.key > x and root.key> y:
            self.__lastCommonAncestor(root.left, x, y)
        elif root.key< x and root.key< y:
            self.__lastCommonAncestor(root.right, x, y)
        else:
            print(root.key)
    

bst = BST(5)
bst.insert(9)
bst.insert(10)
bst.insert(3)
bst.insert(8)
bst.insert(7)
bst.insert(2)
bst.insert(1)
bst.insert(4)
bst.insert(6)
print("InOrder of tree: ")
bst.inorder()
print()
bst.deleteKey(2)
print("InOrder after deleting 2: ")
bst.inorder()
print()
print("Last common ancestor of 6 and 10 is: ")
bst.lastCommonAncestor(6, 10)
print(f"Min value of tree is: {bst.minValue()}")
print(f"Max value of tree is: {bst.maxValue()}")
print("PostOrder of tree is: ")
bst.postorder()
print("\nPreOrder of tree is: ")
bst.preorder()