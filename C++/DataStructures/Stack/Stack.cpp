// Stack.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
using namespace std;
#define MAX 1000

class Stack {
    int top;
public:
    int a[MAX];

    Stack() { top = -1; }
    bool push(int data);
    int pop();
    int search(int key);
};

bool Stack::push(int data) {
    if (top >= (MAX - 1)) {
        cout << "Stack Overflow";
        return false;
    }
    else {
        a[++top] = data;
        cout << data << " pushed into stack\n";
        return true;
    }
}

int Stack::pop() {
    if (top < 0) {
        cout << "StackUnderflow";
        return 0;
    }
    else {
        return a[top--];
    }
}

int Stack::search(int key) {
    for (int i = 0; i < sizeof(a)/sizeof(a[0]); i++)
    {
        if (a[i] == key)return(top - i);
    }
    return -1;
}
int main()
{
    
    class Stack s;
    s.push(10);
    s.push(20);
    s.push(30);
    cout << s.pop() << " Popped from stack\n";

    cout << "Is 10 in stack? ";
    int index = s.search(10);
    index != -1 ? cout << "Yes, at a distance of " << index << " from top element." : cout << "No.";

    return 0;

}

