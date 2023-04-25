using SortingAlgos.BucketSort;

float[] array = { (float)0.897, (float)0.565, (float)0.656, (float)0.1234, (float)0.665, (float)0.3434 };
BucketSort bucketSort = new();
bucketSort.BucketSorting(array, array.Length);

foreach (var element in array)
{
    Console.Write(element + " ");
}
Console.WriteLine();

Console.WriteLine("".PadLeft(20, '*'));

float[] arr = { (float)9.8, (float)0.6, (float)10.1, (float)1.9, (float)3.07, (float)3.04, (float)5.0, (float)8.0, (float)4.8, (float)7.68 };
BucketSortForNumbersWithIntegerPart integerPart = new();
integerPart.BucketSort(arr, 5);

foreach (var element in arr) Console.Write(element+" ");    