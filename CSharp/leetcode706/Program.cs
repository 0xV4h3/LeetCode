namespace leetcode706
{
    //706. Design HashMap
    public class MyHashMap
    {
        private List<List<KeyValuePair<int, int>>> _buckets;
        private int _capacity = 1000;

        public MyHashMap()
        {
            _buckets = new List<List<KeyValuePair<int, int>>>(_capacity);
            for (int i = 0; i < _capacity; i++)
            {
                _buckets.Add(new List<KeyValuePair<int, int>>());
            }
        }

        public void Put(int key, int value)
        {
            int index = key.GetHashCode() & 0x7fffffff;
            index %= _capacity;
            var bucket = _buckets[index];
            for (int i = 0; i < bucket.Count; i++)
            {
                if (bucket[i].Key == key)
                {
                    bucket[i] = new KeyValuePair<int, int>(key, value);
                    return;
                }
            }
            bucket.Add(new KeyValuePair<int, int>(key, value));
        }

        public int Get(int key)
        {
            int index = key.GetHashCode() & 0x7fffffff;
            index %= _capacity;
            var bucket = _buckets[index];
            foreach (var kvp in bucket)
            {
                if (kvp.Key == key)
                    return kvp.Value;
            }
            return -1;
        }

        public void Remove(int key)
        {
            int index = key.GetHashCode() & 0x7fffffff;
            index %= _capacity;
            var bucket = _buckets[index];
            for (int i = 0; i < bucket.Count; i++)
            {
                if (bucket[i].Key == key)
                {
                    bucket.RemoveAt(i);
                    return;
                }
            }
        }
    }
    public class Program
    {
        static void Main(string[] args)
        {
            MyHashMap myHashMap = new();
            myHashMap.Put(1, 1); // The map is now [[1,1]]
            myHashMap.Put(2, 2); // The map is now [[1,1], [2,2]]
            Console.WriteLine(myHashMap.Get(1)); // return 1, The map is now [[1,1], [2,2]]
            Console.WriteLine(myHashMap.Get(3)); // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
            myHashMap.Put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
            Console.WriteLine(myHashMap.Get(2)); // return 1, The map is now [[1,1], [2,1]]
            myHashMap.Remove(2); // remove the mapping for 2, The map is now [[1,1]]
            Console.WriteLine(myHashMap.Get(2)); // return -1 (i.e., not found), The map is now [[1,1]]
        }
    }
}
