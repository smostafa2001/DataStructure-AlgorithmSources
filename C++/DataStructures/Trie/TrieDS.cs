internal class TrieDS
{
    static readonly int ALPHABET_SIZE = 26;
    class TrieNode
    {
        public TrieNode[] children = new TrieNode[ALPHABET_SIZE];
        public bool isEndOfWord;

        public TrieNode()
        {
            isEndOfWord = false;
            for (int i = 0; i < ALPHABET_SIZE; i++)
                children[i] = null;
        }
    };

    static TrieNode root;

    static void Insert(String key)
    {
        int level;
        int length = key.Length;
        int index;

        TrieNode pCrawl = root;

        for (level = 0; level < length; level++)
        {
            index = key[level] - 'a';
            if (pCrawl.children[index] == null)
                pCrawl.children[index] = new TrieNode();

            pCrawl = pCrawl.children[index];
        }


        pCrawl.isEndOfWord = true;
    }

    static bool Search(String key)
    {
        int level;
        int length = key.Length;
        int index;
        TrieNode pCrawl = root;

        for (level = 0; level < length; level++)
        {
            index = key[level] - 'a';

            if (pCrawl.children[index] == null)
                return false;

            pCrawl = pCrawl.children[index];
        }

        return (pCrawl.isEndOfWord);
    }

    public static void Main()
    {
        String[] keys = {"the", "a", "there", "answer",
                        "any", "by", "bye", "their"};

        String[] output = { "Not present in trie", "Present in trie" };


        root = new TrieNode();

        int i;
        for (i = 0; i < keys.Length; i++)
            Insert(keys[i]);

        if (Search("the") == true)
            Console.WriteLine("the --- " + output[1]);
        else Console.WriteLine("the --- " + output[0]);

        if (Search("these") == true)
            Console.WriteLine("these --- " + output[1]);
        else Console.WriteLine("these --- " + output[0]);

        if (Search("their") == true)
            Console.WriteLine("their --- " + output[1]);
        else Console.WriteLine("their --- " + output[0]);

        if (Search("thaw") == true)
            Console.WriteLine("thaw --- " + output[1]);
        else Console.WriteLine("thaw --- " + output[0]);

    }
}
