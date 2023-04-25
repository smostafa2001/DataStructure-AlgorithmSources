#include <iostream>
using namespace std;

class BST {
	int data;
	BST* left, * right;
public:
	BST();
	BST(int);
	BST* insert(BST*, int);
	void inorder(BST*);
	BST* deleteNode(BST*, int);
	BST* minValueNode(BST*);

};

BST::BST() : data(0), left(NULL), right(NULL) {}

BST::BST(int value) {
	data = value;
	left = right = NULL;
}

BST* BST::insert(BST* root, int value) {
	if (!root) {
		return new BST(value);
	}

	if (value > root->data) {
		root->right = insert(root->right, value);
	}

	else if (value < root->data) {
		root->left = insert(root->left, value);
	}

	return root;
}

BST* BST::minValueNode(BST* node) {
	BST* current = node;
	while (current && current->left != NULL)
		current = current->left;
	return current;
}

void BST::inorder(BST* root) {
	if (!root)return;
	inorder(root->left);
	cout << root->data << " ";
	inorder(root->right);
}

BST* BST::deleteNode(BST* root, int key) {
	if (root == NULL)return root;
	if (key < root->data)
		root->left = deleteNode(root->left, key);
	else if (key > root->data)
		root->right = deleteNode(root->right, key);
	else {
		if (root->left == NULL && root->right == NULL)return NULL;
		else if (root->left == NULL) {
			BST* temp = root->right;
			delete root;
			return temp;
		}
		else if (root->right == NULL) {
			BST* temp = root->left;
			delete root;
			return temp;
		}

		BST* temp = BST::minValueNode(root->right);

		root->data = temp->data;
		root->right = deleteNode(root->right, temp->data);
	}
	return root;

}



int main()
{

	BST b, * root = NULL;
	root = b.insert(root, 50);
	b.insert(root, 20);
	b.insert(root, 30);
	b.insert(root, 40);
	b.insert(root, 70);
	b.insert(root, 60);
	b.insert(root, 80);
	cout << "Inorder traversal of the given tree \n";
	b.inorder(root);

	cout << "\nDelete 20\n";
	root = b.deleteNode(root, 20);
	cout << "Inorder traversal of the modified tree \n";
	b.inorder(root);

	cout << "\nDelete 30\n";
	root = b.deleteNode(root, 30);
	cout << "Inorder traversal of the modified tree \n";
	b.inorder(root);

	cout << "\nDelete 50\n";
	root = b.deleteNode(root, 50);
	cout << "Inorder traversal of the modified tree \n";
	b.inorder(root);

	
	return 0;
}

