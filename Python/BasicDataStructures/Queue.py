class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.front = self.size = 0
        self.rear = capacity-1
        self.q = [None]*capacity
    def isFull(self): return self.size == self.capacity
    def isEmpty(self): return self.size == 0
    def addQ(self, x):
        if self.isFull():
            print("Full")
            return
        self.rear = (self.rear+1)%(self.capacity)
        self.q[self.rear]=x
        self.size+=1
        print(f"{x} is enqueued to queue")
    def delQ(self):
        if self.isEmpty():
            print("Empty")
            return
        print(f"{self.q[self.front]} is dequeued from queue")
        self.front = (self.front+1)%(self.capacity)
        self.size -=1
    def getFront(self):
        if self.isEmpty():
            print("Queue is empty")
        print(f"Rear item is: {self.q[self.rear]}")
    def getRear(self):
        if self.isEmpty():
            print("Queue is empty")
        print(f"Front item is: {self.q[self.front]}")      
queue = Queue(30)
queue.addQ(10)
queue.addQ(20)
queue.addQ(30)
queue.addQ(40)
queue.delQ()
queue.getFront()
queue.getRear()