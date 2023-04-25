using SortingAlgos.BubbleSort;

//int[] array = { 5, 1, 4, 2, 8 };
//BubbleSort bubbleSort = new();

//bubbleSort.BubbleSortFunc(array);
//BubbleSort.printArray(array);

//int[] array = { 64, 34, 25, 12, 22, 11, 90 };
//OptimizedBubbleSort bubbleSort = new();
//bubbleSort.BubbleSortOptimized(array);
//OptimizedBubbleSort.printArray(array);

int[] array = { 2, 5, 1, 6, 9 };

RecursiveBubbleSort bubbleSort = new();
bubbleSort.BubbleSortRecursive(array, array.Length);

BubbleSort.printArray(array);