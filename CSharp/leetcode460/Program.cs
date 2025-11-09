namespace leetcode460
{
    //460. LFU Cache
    public class LFUCache
    {
        private class Node
        {
            public int Key;
            public int Value;
            public int Freq;
            public Node(int k, int v)
            {
                Key = k;
                Value = v;
                Freq = 1;
            }
        }

        private readonly int _capacity;
        private int _count;
        private int _minFreq;

        private readonly Dictionary<int, LinkedListNode<Node>> _keyNode = new();

        private readonly Dictionary<int, LinkedList<Node>> _freqList = new();

        public LFUCache(int capacity)
        {
            _capacity = capacity;
            _count = 0;
            _minFreq = 0;
        }

        public int Get(int key)
        {
            if (_capacity <= 0) return -1;
            if (!_keyNode.TryGetValue(key, out var nodeRef)) return -1;

            IncreaseFrequency(nodeRef);
            return nodeRef.Value.Value;
        }

        public void Put(int key, int value)
        {
            if (_capacity <= 0) return;

            if (_keyNode.TryGetValue(key, out var nodeRef))
            {
                nodeRef.Value.Value = value;
                IncreaseFrequency(nodeRef);
                return;
            }

            if (_count >= _capacity)
            {
                if (_freqList.TryGetValue(_minFreq, out var list) && list.Count > 0)
                {
                    var toRemove = list.Last;
                    list.RemoveLast();
                    _keyNode.Remove(toRemove.Value.Key);
                    _count--;
                }
            }

            var newNode = new Node(key, value);
            if (!_freqList.TryGetValue(1, out var freqOneList))
            {
                freqOneList = new LinkedList<Node>();
                _freqList[1] = freqOneList;
            }
            var newNodeRef = freqOneList.AddFirst(newNode);
            _keyNode[key] = newNodeRef;
            _count++;
            _minFreq = 1;
        }

        private void IncreaseFrequency(LinkedListNode<Node> nodeRef)
        {
            int oldFreq = nodeRef.Value.Freq;
            int newFreq = oldFreq + 1;

            if (_freqList.TryGetValue(oldFreq, out var oldList))
            {
                oldList.Remove(nodeRef);
                if (oldList.Count == 0)
                {
                    _freqList.Remove(oldFreq);
                    if (_minFreq == oldFreq) _minFreq = newFreq;
                }
            }

            nodeRef.Value.Freq = newFreq;
            if (!_freqList.TryGetValue(newFreq, out var newList))
            {
                newList = new LinkedList<Node>();
                _freqList[newFreq] = newList;
            }
            var newNodeRef = newList.AddFirst(nodeRef.Value);

            _keyNode[nodeRef.Value.Key] = newNodeRef;
        }
    }

    public class Program
    {
        static void Main(string[] args)
        {
            LFUCache lfu = new(2);
            lfu.Put(1, 1); // cache=[1,_], cnt(1)=1
            lfu.Put(2, 2); // cache=[2,1], cnt(2)=1, cnt(1)=1
            Console.WriteLine(lfu.Get(1));   // return 1
            lfu.Put(3, 3); // cache=[3,1], cnt(3)=1, cnt(1)=2
            Console.WriteLine(lfu.Get(2));    // returns -1 (not found)
            Console.WriteLine(lfu.Get(3));    // return 3, cache=[3,1], cnt(3)=2, cnt(1)=2
            lfu.Put(4, 4); // cache=[4,3], cnt(4)=1, cnt(3)=2
            Console.WriteLine(lfu.Get(1));    // return -1 (not found)
            Console.WriteLine(lfu.Get(3));    // return 3, cache=[3,4], cnt(4)=1, cnt(3)=3
            Console.WriteLine(lfu.Get(4));    // return 4, cache=[4,3], cnt(4)=2, cnt(3)=3
        }
    }
}