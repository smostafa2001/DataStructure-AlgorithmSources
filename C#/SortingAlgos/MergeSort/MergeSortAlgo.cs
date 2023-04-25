namespace MergeSort
{
    public class MergeSortAlgo
    {

        static void merge(int[] array, int left, int mid, int right)
        {
            var subArrayOne = mid - left + 1;
            var subArrayTwo = right - mid;

            var leftArray = new int[subArrayOne];
            var rightArray = new int[subArrayTwo];

            for (int i = 0; i < subArrayOne; i++)
            {
                leftArray[i] = array[left + i];
            }
            for (int i = 0; i < subArrayTwo; i++)
            {
                rightArray[i] = array[mid + 1 + i];
            }

            var indexOfSubArrayOne = 0;
            var indexOfSubArrayTwo = 0;
            var indexOfMergedArray = left;

            while (indexOfSubArrayOne < subArrayOne && indexOfSubArrayTwo < subArrayTwo)
            {
                if (leftArray[indexOfSubArrayOne] <= rightArray[indexOfSubArrayTwo])
                {
                    array[indexOfMergedArray] = leftArray[indexOfSubArrayOne];
                    indexOfSubArrayOne++;
                }
                else
                {
                    array[indexOfMergedArray] = rightArray[indexOfSubArrayTwo];
                    indexOfSubArrayTwo++;
                }
                indexOfMergedArray++;
            }

            while (indexOfSubArrayOne < subArrayOne)
            {
                array[indexOfMergedArray] = leftArray[indexOfSubArrayOne];
                indexOfSubArrayOne++;
                indexOfMergedArray++;
            }

            while (indexOfSubArrayTwo < subArrayTwo)
            {
                array[indexOfMergedArray] = rightArray[indexOfSubArrayTwo];
                indexOfSubArrayTwo++;
                indexOfMergedArray++;
            }
        }

        static void Sort(int[] array, int begin, int end)
        {
            if (begin >= end) return;

            var mid = begin + (end - begin) / 2;
            Sort(array, begin, mid);
            Sort(array, mid + 1, end);
            merge(array, begin, mid, end);
        }

        static void printArray(int[] array)
        {
            foreach (var item in array)
            {
                Console.Write(item + " ");
            }
            Console.WriteLine();
        }
        static void Main(string[] args)
        {
            int[] arr = { 12, 11, 13, 5, 6, 7 };
            var arraySize = arr.Length;

            Console.WriteLine("Given array is:");
            printArray(arr);

            Sort(arr, 0, arraySize - 1);

            Console.WriteLine("\nSorted array is:");
            printArray(arr);
        }
    }
}