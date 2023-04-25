
#include <iostream>
using namespace std;

class Queue {
public:
    int front, rear, size;
    unsigned capacity;
    int* array;
};

Queue* createQueue(unsigned capacity) {
    Queue* queue = new Queue();
    queue->capacity = capacity;
    queue->front = queue->size = 0;

    queue->rear = capacity - 1;
    queue->array = new int[queue->capacity];
    return queue;
}

int search(Queue* queue, int key) {
    for (int i = 0; i <= queue->size;i++) {
        if (queue->array[i] == key)return i - queue->front;
    }
    return -1;
}

bool isFull(Queue* queue) {
    return(queue->size == queue->capacity);
}

bool isEmpty(Queue* queue) {
    return(queue->size == 0);
}

void enqueue(Queue* queue, int item) {
    if (isFull(queue))return;
    queue->rear = (queue->rear + 1) % queue->capacity;
    queue->array[queue->rear] = item;
    queue->size = queue->size + 1;
    cout << item << " enqueued to queue\n";
}

int dequeue(Queue* queue) {
    if (isEmpty(queue))return INT_MIN;
    int item = queue->array[queue->front];
    queue->front = (queue->front + 1) % queue->capacity;
    queue->size = queue->size - 1;
    return item;
}

int front(Queue* queue) {
    if (isEmpty(queue))return INT_MIN;
    return queue->array[queue->front];
}

int rear(Queue* queue) {
    if (isEmpty(queue))
        return INT_MIN;
    return queue->array[queue->rear];
}
int main()
{
    Queue* queue = createQueue(1000);

    enqueue(queue, 10);
    enqueue(queue, 20);
    enqueue(queue, 30);
    enqueue(queue, 40);

    cout << dequeue(queue) << " dequeued from queue\n";

    cout << "Front item is " << front(queue) << endl;

    cout << "Rear item is " << rear(queue) << endl;

    cout << "Is 40 in queue? ";
    int index = search(queue, 40);
    index != -1 ? cout << "Yes,  at a distance of " << index << " from front element.\n" : cout << "No."<<endl;
    index = search(queue, 10);
    cout << "Is 10 in queue? ";
    index != -1 ? cout << "Yes,  at a distance of " << index << " from front element." : cout << "No.";
    return 0;
}

