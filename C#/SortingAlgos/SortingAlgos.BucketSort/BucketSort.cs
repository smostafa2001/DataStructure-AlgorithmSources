using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SortingAlgos.BucketSort
{
    public class BucketSort
    {
        public void BucketSorting(float[] array, int length)
        {
            if (length <= 0) return;

            var buckets = new List<float>[length];

            for (int i = 0; i < length; i++)
            {
                buckets[i] = new();
            }

            for (int i = 0; i < length; i++)
            {
                int indexInBucket = (int)array[i] * length;
                buckets[indexInBucket].Add(array[i]);
            }

            for (int i = 0; i < length; i++)
            {
                buckets[i].Sort();
            }

            var index = 0;
            for (int i = 0; i < length; i++)
            {
                for (int j = 0; j < buckets[i].Count; j++)
                {
                    array[index++] = buckets[i][j];
                }
            }
        }
    }
}
