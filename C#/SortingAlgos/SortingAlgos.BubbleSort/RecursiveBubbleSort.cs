using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SortingAlgos.BubbleSort
{
    public class RecursiveBubbleSort
    {
        public void BubbleSortRecursive(int[] array, int length)
        {
            if (length == 0 || length == 1) return;

            for (int i = 0; i < length - 1; i++)
                if (array[i] > array[i + 1]) swap(array, i, i + 1);
            BubbleSortRecursive(array, length - 1);

        }

        private void swap(int[] array, int i, int j)
        {
            int temp = array[i];
            array[i] = array[j];
            array[j] = temp;
        }
    }
}
