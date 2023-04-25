class DoubleEndedQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.q = [None]*capacity
        self.front=self.size=0
        self.rear = capacity -1
    def isFull(self):
        return self.size == self.capacity
    def isEmpty(self): return self.size == 0
    def addLast(self,x):
        if self.isFull():
            print("Full")
            return
        self.rear = (self.rear+1)%(self.capacity)
        self.q[self.rear]=x
        self.size+=1
        print(f"{x} is added in last of queue")
    def addFront(self,x):
        if self.isFull():
            print("Queue overflow")
            return
        self.front = (self.front-1)%(self.capacity)
        self.q[self.front]=x
        self.size+=1
        print(f"{x} is added in front of queue")
    def delFront(self):
        if self.isEmpty():
            print("Empty")
            return
        x=self.q[self.front]
        print(f"{x} is deleted from front of queue")
        self.front = (self.front+1)%(self.capacity)
        self.size -=1
        return x
    def delLast(self):
        if self.isEmpty():
            print("Empty")
            return
        x = self.q[self.rear]
        print(f"{x} is deleted from last of queue")
        self.rear = (self.rear-1)%(self.capacity)
        self.size-=1
        return x
    def getFront(self):
        if self.isEmpty():
            print("Queue is empty")
        print(f"Front item is: {self.q[self.front]}")
    def getRear(self):
        if self.isEmpty():
            print("Queue is empty")
        print(f"Rear item is: {self.q[self.rear]}")      
        
deque = DoubleEndedQueue(7)
deque.addFront(1)
deque.addLast(2)
deque.addFront(4)
print(f"Queue size is: {deque.size}")   
deque.addLast(0)
deque.getFront()
deque.delFront()
deque.getRear()
deque.delLast()
deque.delLast()
deque.delLast()
print(f"Queue size is: {deque.size}")

