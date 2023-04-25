#include <iostream>
using namespace std;

void insertionSort(int arr[], int arrayLength) 
{
	for (int i = 1; i < arrayLength; i++)
	{
		int key = arr[i];
		int j = i - 1;
		while (j >= 0 && arr[j] < key) 
		{
			arr[j + 1] = arr[j];
			j = j - 1;
		}
		arr[j + 1] = key;
	}
}

void printArray(int arr[], int arrayLength)
{
	for (int i = 0; i < arrayLength; i++)
	{
		cout << arr[i] << " ";
	}
	cout << "\n";
	
}

int main()
{
	//int x = 10;
	//int y = 5;
	//int z = ++x + y / 2 * 4 + --y - x++;
	int x = 10;
	int y = 5;
	int q = ++x * ++x;
	cout << q <<"\n";
	//int arr[] = { 12, 11, 100, 45, 17, 74, 13, 11, 5, 6 };
	//int arrayLength = sizeof(arr) / sizeof(arr[0]);
	//insertionSort(arr, arrayLength);
	//printArray(arr, arrayLength);
}

