using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SortingAlgos.BubbleSort
{
    public class OptimizedBubbleSort
    {
        public void BubbleSortOptimized(int[] array)
        {
            for (int i = 0; i < array.Length-1; i++)
            {
                bool isSwapped = false;

                for(int j = 0; j < array.Length-i-1; j++)
                {
                    if (array[j] > array[j + 1])
                    {
                        int temp = array[j];
                        array[j] = array[j + 1];
                        array[j + 1] = temp;
                        isSwapped = true;

                    }
                }

                if (!isSwapped) break;
            }
        }

        public static void printArray(int[] array)
        {
            for (int i = 0; i < array.Length; i++)
            {
                Console.Write(array[i]+" ");
            }
            Console.WriteLine();
        }
    }
}
