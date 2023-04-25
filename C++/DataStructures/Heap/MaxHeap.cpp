#include <iostream>
using namespace std;

class MaxHeap {
    int* arr;

    int maxSize;

    int heapSize;

public:
    MaxHeap(int maxSize);

    void MaxHeapify(int);

    int parent(int index) {
        return (index - 1) / 2;
    }

    int leftChild(int index) {
        return(2 * index + 1);
    }

    int rightChild(int index) {
        return(2 * index + 2);
    }

    int removeMax();

    void increaseKey(int index, int newValue);

    int getMax() {
        return arr[0];
    }

    int currentSize() {
        return heapSize;
    }

    void deleteKey(int index);
    
    void insertKey(int key);

    int search(int key);
    void display();
};

MaxHeap::MaxHeap(int toTheSize) {
    heapSize = 0;
    maxSize = toTheSize;
    arr = new int[toTheSize];
}

void MaxHeap::insertKey(int key) {
    if (heapSize == maxSize) {
        cout << "\nOverflow: Could not insertKey\n";
        return;
    }

    heapSize++;
    int index = heapSize - 1;
    arr[index] = key;

    while (index != 0 && arr[parent(index)] < arr[index]) {
        swap(arr[index], arr[parent(index)]);
        index = parent(index);
    }
}

void MaxHeap::increaseKey(int index, int newValue) {
    arr[index] = newValue;
    while (index != 0 && arr[parent(index)] < arr[index]) {
        swap(arr[index], arr[parent(index)]);
        index = parent(index);
    }
}

int MaxHeap::removeMax() {
    if (heapSize <= 0)return INT_MIN;
    if (heapSize == 1) {
        heapSize--;
        return arr[0];
    }

    int root = arr[0];

    arr[0] = arr[heapSize - 1];
    heapSize--;

    MaxHeapify(0);

    return root;
}

void MaxHeap::deleteKey(int index) {
    increaseKey(index, INT_MAX);
    removeMax();
}

void MaxHeap::MaxHeapify(int index) {
    int left = leftChild(index);
    int right = rightChild(index);
    int largest = index;
    if (left<heapSize && arr[left]>arr[largest])largest = left;
    if (right<heapSize && arr[right]>arr[largest])largest = right;
    if (largest != index) {
        swap(arr[index], arr[largest]);
        MaxHeapify(largest);
    }
}

void MaxHeap::display() {
    for (int i = 0; i < heapSize;i++)cout << arr[i] << " ";
    cout << endl;
}

int MaxHeap::search(int key) {
    for (int i = 0; i < heapSize;i++) {
        if (arr[i] == key)return i;
    }
    return -1;
}
int main()
{
    MaxHeap heap(15);

    heap.insertKey(3);
    heap.insertKey(10);
    heap.insertKey(12);
    heap.insertKey(8);
    heap.insertKey(2);
    heap.insertKey(14);

    cout << "The current size of the heap is " << heap.currentSize() << endl;

    cout << "The current maximum element is " << heap.getMax() << endl;

    cout << "The heap is: ";
    heap.display();

    heap.deleteKey(2);

    cout << "The current size of the heap (after deleting index 2) is " << heap.currentSize() << endl;

    cout << "The current maximum element (after deleting index 2) is " << heap.getMax() << endl;

    cout << "The heap (after deleting index 2) is: ";
    heap.display();

    cout << "Is 2 in the heap? ";
    int index = heap.search(2);
    index != -1 ? cout << "Yes, in the index of " << index << endl:cout<<"No\n";

    cout << "Is 7 in the heap? ";
    index = heap.search(7);
    index != -1 ? cout << "Yes, in the index of " << index << endl : cout << "No\n";


}

