using System.Collections.Generic;

namespace leetcode_705
{
    //705. Design HashSet
    public class MyHashSet
    {
        private List<List<int>> _buckets;
        private int _capacity = 10;
        public MyHashSet()
        {
            _buckets = new List<List<int>>(_capacity);
            for (int i = 0; i < _capacity; i++)
            {
                _buckets.Add(new List<int>());
            }
        }

        public void Add(int key)
        {
            int index = key.GetHashCode() & 0x7fffffff;
            index %= _capacity;
            var bucket = _buckets[index];
            for (int i = 0; i < bucket.Count; i++)
            {
                if (bucket[i] == key) return;
            }
            bucket.Add(key);
        }

        public void Remove(int key)
        {
            int index = key.GetHashCode() & 0x7fffffff;
            index %= _capacity;
            var bucket = _buckets[index];
            for (int i = 0; i < bucket.Count; i++)
            {
                if (bucket[i] == key)
                {
                    bucket.RemoveAt(i);
                    return;
                }
            }
        }

        public bool Contains(int key)
        {
            int index = key.GetHashCode() & 0x7fffffff;
            index %= _capacity;
            var bucket = _buckets[index];
            for (int i = 0; i < bucket.Count; i++)
            {
                if (bucket[i] == key)
                    return true;
            }
            return false;
        }
    }
    public class Program
    {
        static void Main(string[] args)
        {
            MyHashSet myHashSet = new MyHashSet();
            myHashSet.Add(1);      // set = [1]
            myHashSet.Add(2);      // set = [1, 2]
            Console.WriteLine(myHashSet.Contains(1)); // return True
            Console.WriteLine(myHashSet.Contains(3)); // return False, (not found)
            myHashSet.Add(2);      // set = [1, 2]
            Console.WriteLine(myHashSet.Contains(2)); // return True
            myHashSet.Remove(2);   // set = [1]
            Console.WriteLine(myHashSet.Contains(2)); // return False, (already removed)
        }
    }
}
