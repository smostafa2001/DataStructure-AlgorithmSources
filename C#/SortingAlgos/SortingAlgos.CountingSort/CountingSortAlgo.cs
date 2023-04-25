using System;
using System.Linq;

namespace SortingAlgos.CountingSort
{
    public class CountingSortAlgo
    {
        static void Main(string[] args)
        {
            int[] arr = { -5, -10, 0, -3, 8, 5, -1, 10 };
            CountingSort(arr);
            foreach (int i in arr)
            {
                Console.Write(i + " ");
            }
        }


        public static void CountingSort(int[] inputArray)
        {
            int maxElement = inputArray.Max();
            int minElement = inputArray.Min();
            int rangeOfElements = maxElement - minElement + 1;
            int[] count = new int[rangeOfElements];
            int[] outputArray = new int[inputArray.Length];
            for (int i = 0; i < inputArray.Length; i++)
            {
                count[inputArray[i] - minElement]++;
            }
            for (int i = 1; i < count.Length; i++)
            {
                count[i] += count[i - 1];
            }

            for (int i = inputArray.Length - 1; i >= 0; i--)
            {
                outputArray[count[inputArray[i] - minElement] - 1] = inputArray[i];
                count[inputArray[i] - minElement]--;
            }
            for (int i = 0; i < inputArray.Length; i++)
            {
                inputArray[i] = outputArray[i];
            }

        }
    }



}

