namespace SortingAlgos.InsertionSort
{
    public class InsertionSortAlgo
    {
        static void Main(string[] args)
        {
            int[] array = { 12, 11, 100, 45, 17, 74, 13, 11, 5, 6 };
            InsertionSortAlgo obj = new InsertionSortAlgo();
            obj.InsertionSort(array);
            printArray(array);
        }
        public void InsertionSort(int[] array)
        {
            int arrayLength = array.Length;
            for (int i = 1; i < arrayLength; i++)
            {
                int key = array[i];
                int j = i - 1;
                while (j >= 0 && array[j] < key)
                {
                    array[j + 1] = array[j];
                    j = j - 1;
                }
                array[j + 1] = key;
            }
        }

        public static void printArray(int[] array)
        {
            int arrayLength = array.Length;
            for (int i = 0; i < arrayLength; i++)
            {
                Console.Write(array[i] + " ");
            }
            Console.Write("\n");
        }

    }


}