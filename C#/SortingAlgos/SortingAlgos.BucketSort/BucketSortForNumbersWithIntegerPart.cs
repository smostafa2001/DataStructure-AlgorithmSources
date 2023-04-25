using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Cryptography;
using System.Text;
using System.Threading.Tasks;

namespace SortingAlgos.BucketSort
{
    public class BucketSortForNumbersWithIntegerPart
    {
        public void BucketSort(float[] array, int numberOfBuckets)
        {
            var maxElement = array.Max();
            var minElement = array.Min();

            var range = (maxElement - minElement) / numberOfBuckets;

            var temp = new List<List<float>>();

            for (int i = 0; i < numberOfBuckets; i++)
            {
                temp.Add(new List<float>());
            }


            for (int i = 0; i < array.Length; i++)
            {
                var diff = (array[i] - minElement) / range - (int)((array[i] - minElement) / range);

                if (diff == 0 && array[i] != minElement) temp[(int)((array[i] - minElement) / range) - 1].Add(array[i]);
                else temp[(int)((array[i] - minElement) / range)].Add(array[i]);
            }

            for (int i = 0; i < temp.Count; i++)
            {
                if (temp[i].Count != 0) temp[i].Sort();

                int index = 0;
                foreach (var list in temp)
                {
                    if (list is not null)
                    {
                        foreach (var item in list)
                        {
                            array[index++] = item;
                        }
                    }
                }
            }
        }
    }
}
