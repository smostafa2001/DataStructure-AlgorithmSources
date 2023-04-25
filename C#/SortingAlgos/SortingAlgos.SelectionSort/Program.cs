using SortingAlgos.SelectionSort;

int[] array = { 64, 25, 12, 22, 11 };
SelectionSort selectionSort = new();
selectionSort.Sort(array);

for (int i = 0; i < array.Length; i++)
{
    Console.Write(array[i]+" ");
}