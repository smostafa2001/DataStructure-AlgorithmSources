class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data,end=" ")
            temp = temp.next
    def insertFirst(self, x):
        newNode = Node(x)
        newNode.next = self.head
        self.head = newNode
    def insertAfter(self, w,x):
        if w is None:
            print("The given previous node must be in linkedList.")
            return
        newNode=Node(x)
        newNode.next = w.next
        w.next = newNode
    def insertLast(self, x):
        newNode=Node(x)
        if self.head is None:
            self.head = newNode
            return
        last = self.head
        while(last.next):
            last = last.next
        last.next = newNode
    def deleteFirst(self):
        if not self.head:
            return None
        temp = self.head
        self.head = self.head.next
        return temp
    def deleteLast(self):
        if self.head is None:
            return None
        if self.head.next is None:
            temp = self.head
            self.head = None
            return temp
        secondLast = self.head
        while secondLast.next.next:
            secondLast = secondLast.next
        temp = secondLast.next
        secondLast.next = None
        return temp
        
    def delete(self, x):
        y = self.head
        if y is not None:
            if y.data == x:
                self.head = y.next
                y = None
                return
        while(y is not None):
            if y.data == x: break
            w = y
            y = y.next
        if y is None: return
        w.next = y.next
        y = None
    def search(self, x):
        y = self.head
        index = 0
        while (y.data != x and y.next is not None):
            index+=1
            y = y.next

        if (y.data != x):
            return False
        return index

        
        
list = LinkedList()
list.insertLast(6)
list.insertFirst(7)
list.insertFirst(1)
list.insertLast(4)
list.insertAfter(list.head.next, 8)
list.delete(8)
list.deleteFirst()
list.deleteLast()
print(list.search(4))
list.printList()
