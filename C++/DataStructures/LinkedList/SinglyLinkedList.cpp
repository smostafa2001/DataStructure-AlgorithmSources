// LinkedList.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
using namespace std;
class Node {
public:
	int data;
	Node* next;
};
void push(Node** head, int newData) {
	Node* newNode = new Node();
	newNode->data = newData;
	newNode->next = *head;
	*head = newNode;
}

void insertAfter(Node* prevNode, int newData) {
	if (prevNode == NULL) {
		cout << "The give previous nde can't be NULL";
		return;
	}

	Node* newNode = new Node();
	newNode->data = newData;
	newNode->next = prevNode->next;
	prevNode->next = newNode;
}

void append(Node** head, int newData) {
	Node* newNode = new Node();
	Node* last = *head;
	newNode->data = newData;
	newNode->next = NULL;

	if (*head == NULL) {
		*head = newNode;
		return;
	}

	while (last->next != NULL) {
		last = last->next;
	}

	last->next = newNode;
	return;
}

void deleteNode(Node** head, int key) {
	Node* temp = *head;
	Node* prev = NULL;

	if (temp != NULL && temp->data == key) {
		*head = temp->next;

		delete temp;
		return;
	}

	else {
		while (temp != NULL && temp->data != key) {
			prev = temp;
			temp = temp->next;
		}

		if (temp == NULL)return;

		prev->next = temp->next;

		delete temp;
	}
}

int search(Node** head, int key) {
	Node* temp = *head;
	int index = 0;
	while (temp->data != key && temp->next != NULL) {
		index++;
		temp = temp->next;
	}

	if (temp->data != key)
		return -1;
	return index;
}

void display(Node* node) {

	while (node != NULL) {
		cout << node->data << " ";
		node = node->next;
	}

}


int main()
{
	Node* head = NULL;

	append(&head, 5);

	push(&head, 6);

	push(&head, 1);

	append(&head, 4);

	insertAfter(head->next, 8);

	cout << "Linked list is: ";
	display(head);

	deleteNode(&head, 1);
	cout << "\nLinked List after Deletion of 1: ";
	display(head);

	cout << "\nIs 22 in Linked list? ";
	int index = search(&head, 22);
		index !=-1 ? cout << "Yes, at the index "<<index : cout << "No";
	cout << "\nIs 6 in Linked list? ";
	index = search(&head, 6);
	index !=-1 ? cout << "Yes, at the index "<<index : cout << "No";

	return 0;
}

