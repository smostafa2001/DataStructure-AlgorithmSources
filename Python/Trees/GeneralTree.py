class Node:
    def __init__(self, key):
        self.parent = None
        self.leftChild = None
        self.rightSibling = None
        self.key = key
class Tree:
    def __init__(self, key):
        self.root = Node(key)
    def isEmpty(self):
        return self.root is None
    def addSibling(self, sibling, key):
        if sibling == None: return None
        while sibling.rightSibling:
            sibling = sibling.rightSibling
        sibling.rightSibling = Node(key)
        return sibling
    def addChild(self, parent, key):
        if parent == None:
            return None
        if parent.leftChild:
            return self.addSibling(parent.leftChild, key)
        else:
            parent.leftChild = Node(key)
            return parent
    def findInSubtree(self, key, node):
        if node.key == key:
            return node
        child = node.leftChild
        while child is not None:
            result = self.findInSubtree(key, child)
            if result is not None:
                return result
            child = child.rightSibling
        return None
    def findByKey(self, key):
        if self.isEmpty(): return None
        return self.findInSubtree(key, self.root)
    def addNewNodeByKey(self, parentKey, key):
        return self.addChild(self.findByKey(parentKey),key)
    def getSubtreeSize(self, node):
        if node is None:
            return 0
        count = 1
        child = node.leftChild
        while child is not None:
            count += self.getSubtreeSize(child)
            child = child.rightSibling
        return count
    def getSize(self):
        if self.isEmpty():
            return 0
        return self.getSubtreeSize(self.root)
    def preOrder(self, node):
        if node is None: return
        print(node.key,end=" ")
        self.preOrder(node.leftChild)
        self.preOrder(node.rightSibling)

    def postOrder(self,node):
        if node is None: return
        self.postOrder(node.leftChild)
        self.postOrder(node.rightSibling)
        print(node.key,end=" ")

    def inOrder(self, node):
        if node is None: return
        self.inOrder(node.leftChild)
        print(node.key,end=" ")
        self.inOrder(node.rightSibling)

tree = Tree(3)
tree.addNewNodeByKey(3, 9)
tree.addNewNodeByKey(9, 2)
tree.addNewNodeByKey(3, 4)
tree.addNewNodeByKey(4, 10)
tree.addNewNodeByKey(4, 6)
tree.addNewNodeByKey(4, 5)
tree.addNewNodeByKey(2, 8)
tree.addNewNodeByKey(6, 7)
tree.addNewNodeByKey(8, 1)

print(tree.findByKey(2))
print(tree.getSize())
print("Traverse PreOrder: ",end="")
tree.preOrder(tree.root)
print()
print("Traverse InOrder: ",end="")
tree.inOrder(tree.root)
print()
print("Traverse PostOrder: ",end="")
tree.postOrder(tree.root)

        
        
    