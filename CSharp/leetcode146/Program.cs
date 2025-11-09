namespace leetcode146
{
    //146. LRU Cache
    public class LRUCache
    {
        private readonly int _capacity;
        private readonly LinkedList<KeyValuePair<int, int>> _list = new();
        private readonly Dictionary<int, LinkedListNode<KeyValuePair<int, int>>> _cacheMap = new();

        public LRUCache(int capacity)
        {
            _capacity = capacity;
        }

        public int Get(int key)
        {
            if (_capacity <= 0) return -1;

            if (!_cacheMap.TryGetValue(key, out var node))
                return -1;

            _list.Remove(node);
            _list.AddFirst(node);

            return node.Value.Value;
        }

        public void Put(int key, int value)
        {
            if (_capacity <= 0) return;

            if (_cacheMap.TryGetValue(key, out var existingNode))
            {
                existingNode.Value = new KeyValuePair<int, int>(key, value);
                _list.Remove(existingNode);
                _list.AddFirst(existingNode);
            }
            else
            {
                if (_cacheMap.Count >= _capacity)
                {
                    var lru = _list.Last;
                    if (lru != null)
                    {
                        _cacheMap.Remove(lru.Value.Key);
                        _list.RemoveLast();
                    }
                }

                var newNode = new LinkedListNode<KeyValuePair<int, int>>(new KeyValuePair<int, int>(key, value));
                _list.AddFirst(newNode);
                _cacheMap[key] = newNode;
            }
        }
    }

    public class Program
    {
        static void Main(string[] args)
        {
            LRUCache lru = new(2);
            lru.Put(1, 1); // cache is {1=1}
            lru.Put(2, 2); // cache is {1=1, 2=2}
            Console.WriteLine(lru.Get(1));   // return 1
            lru.Put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
            Console.WriteLine(lru.Get(2));    // returns -1 (not found)
            lru.Put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
            Console.WriteLine(lru.Get(1));    // return -1 (not found)
            Console.WriteLine(lru.Get(3));    // return 3
            Console.WriteLine(lru.Get(4));    // return 4
        }
    }
}
