class Stack:
    def __init__(self, maxSize):
        self.top = -1
        self.maxSize = maxSize
        self.s = [None] * maxSize
    def isEmpty(self):
        return self.top<0
    def push(self,x):
        if(self.top>=self.maxSize-1):
            print("Stack Overflow")
            return False
        self.top+=1
        self.s[self.top] = x
        print(f"{x} pushed into stack")
        return True
    def pop(self):
        if self.top < 0:
            print("Stack Underflow")
            return False
        x = self.s[self.top]
        self.top-=1
        return x
s = Stack(100)
s.push(10)
s.push(20)
s.push(30)
print(f"{s.pop()} Popped from stack")

