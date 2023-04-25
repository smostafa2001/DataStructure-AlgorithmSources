from math import inf
class MaxHeap:
    def __init__(self, maxSize):
        self.heapSize = 0
        self.maxSize = maxSize
        self.array = [None for i in range(maxSize)]
    def parent(self, index):
        return (index-1)//2
    def leftChild(self, index):
        return 2*index+1
    def rightChild(self, index):
        return 2*index+2
    def getMax(self):
        return self.array[0]
    def currentSize(self):
        return self.heapSize
    def insertKey(self, key):
        if self.heapSize == self.maxSize:
            print("Overflow: Could not insert key!")
            return
        self.heapSize+=1
        index = self.heapSize -1
        self.array [index] = key
        while index != 0 and self.array[self.parent(index)]<self.array[index]:
            self.array[index], self.array[self.parent(index)] = self.array[self.parent(index)], self.array[index]
            index = self.parent(index)
    def increaseKey(self, index, newValue):
        if index < 0: return
        self.array[index] = newValue
        while index != 0 and self.array[self.parent(index)] < self.array[index]:
            self.array[index], self.array[self.parent(index)] = self.array[self.parent(index)], self.array[index]
            index = self.parent(index)
    def removeMax(self):
        if self.heapSize <= 0: return -inf
        if self.heapSize == 1:
            self.heapSize-=1
            return self.array[0]
        root = self.array[0]
        self.array[0]=self.array[self.heapSize-1]
        self.heapSize -=1
        self.maxHeapify(0)
        return root
    def deleteByIndex(self, index):
        self.increaseKey(index, inf)
        self.removeMax()
    def deleteKey(self, key):
        self.deleteByIndex(self.search(key))
    def search(self, key):
        for i in range(self.heapSize):
            if self.array[i]==key: return i
        return -1
    def maxHeapify(self, index):
        left = self.leftChild(index)
        right = self.rightChild(index)
        largest = index
        if left<self.heapSize and self.array[left]>self.array[largest]: largest = left
        if right<self.heapSize and self.array[right]>self.array[largest]: largest = right
        if largest != index:
            self.array[index], self.array[largest] = self.array[largest], self.array[index]
            self.maxHeapify(largest)
    def display(self):
        for i in range(self.heapSize):
            print(self.array[i], end=" ")
        print()
heap=MaxHeap(15)

heap.insertKey(3)
heap.insertKey(10)
heap.insertKey(12)
heap.insertKey(8)
heap.insertKey(2)
heap.insertKey(14)
print(f"The current size of the heap is {heap.currentSize()}")
print(f"The current maximum element is {heap.getMax()}")
print("The heap is: ")
heap.display()
heap.deleteKey(2)
print(f"The current size of the heap (after deleting index 2) is {heap.currentSize()}")
print(f"The current maximum element (after deleting index 2) is {heap.getMax()}")
print("The heap (after deleting index 2) is: ")
heap.display()
print("Is 2 in the heap? ")
index = heap.search(2)
print(f"Yes in the index of {index}" if index != -1 else "No")
print("Is 8 in the heap? ")
index = heap.search(8)
print(f"Yes in the index of {index}" if index != -1 else "No")
