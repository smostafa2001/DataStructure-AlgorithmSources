// DoublyLinkedList.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
using namespace std;

class Node {
public:
	Node* prev;
	int data;
	Node* next;
};

void push(Node** head, int newData) {
	Node* newNode = new Node();

	newNode->data = newData;

	newNode->next = *head;
	newNode->prev = NULL;

	if (*head != NULL) (*head)->prev = newNode;

	*head = newNode;
}

void insertAfter(Node* prevNode, int newData) {
	if (prevNode == NULL) {
		cout << "the give previous node can't be NULL";
		return;
	}

	Node* newNode = new Node();

	newNode->data = newData;

	newNode->next = prevNode->next;

	prevNode->next = newNode;

	newNode->prev = prevNode;

	if (newNode->next != NULL)
		newNode->next->prev = newNode;
}

void append(Node** head, int newData) {
	Node* newNode = new Node();

	Node* last = *head;

	newNode->data = newData;

	newNode->next = NULL;

	if (*head == NULL) {
		newNode->prev = NULL;
		*head = newNode;
		return;
	}

	while (last->next != NULL)last = last->next;

	last->next = newNode;

	newNode->prev = last;

}

void insertBefore(Node** head, Node* nextNode, int newData) {
	if (nextNode == NULL) {
		cout << "the give next node can't be NULL";
		return;
	}
	Node* newNode = new Node();

	newNode->data = newData;
	newNode->prev = nextNode->prev;
	nextNode->prev = newNode;
	newNode->next = nextNode;
	if (newNode->prev != NULL) newNode->prev->next = newNode;
	else *head = newNode;
}

void deleteNode(Node** head, Node* item) {
	if (head == NULL || item == NULL)
		return;

	if (*head == item)
		*head = item->next;

	if (item->next != NULL)
		item->next->prev = item->prev;

	if (item->prev != NULL)
		item->prev->next = item->next;

	delete item;
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
	Node* last{};
	cout << "\nTraversal in forward direction \n";
	while (node != NULL) {
		cout << node->data << " ";
		last = node;
		node = node->next;
	}
	cout << "\nTraversal in reverse direction \n";
	while (last != NULL) {
		cout << last->data << " ";
		last = last->prev;
	}


}

int main()
{
	Node* head = NULL;

	append(&head, 5);
	push(&head, 6);
	push(&head, 1);
	append(&head, 3);
	insertAfter(head->next, 8);

	cout << "Double Linked list is: ";
	display(head);

	deleteNode(&head, head->next);
	deleteNode(&head, head->next->next->next);
	cout << "\nDLL after deleting 6 and 3 is: ";
	display(head);

	cout << "\nIs 22 in Linked list? ";
	int index = search(&head, 22);
	index != -1 ? cout << "Yes, at the index " << index : cout << "No";
	cout << "\nIs 8 in Linked list? ";
	index = search(&head, 8);
	index != -1 ? cout << "Yes, at the index " << index : cout << "No";

	return 0;
}
