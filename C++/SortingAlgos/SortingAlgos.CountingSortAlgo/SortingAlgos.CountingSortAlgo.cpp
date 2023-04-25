#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;
void countingSort(vector<int>& inputArray) 
{
	int maxElement = *max_element(inputArray.begin(), inputArray.end());
	int minElement = *min_element(inputArray.begin(), inputArray.end());
	int range = maxElement - minElement + 1;

	vector<int> count(range), output(inputArray.size());
	for (int i = 0; i < inputArray.size(); i++)
	{
		count[inputArray[i] - minElement]++;
	}

	for (int i = 0; i < count.size(); i++)
	{
		count[i] += count[i - 1];
	}
}
int main()
{
	cout << "Hello World!\n";
}

