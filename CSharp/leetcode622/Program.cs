using System.Drawing;
using static System.Net.Mime.MediaTypeNames;

namespace leetcode622
{
    //622. Design Circular Queue
    public class MyCircularQueue
    {
        private int[] _queue;
        private int _front;
        private int _size;
        private int _capacity;

        public MyCircularQueue(int k)
        {
            _capacity = k;
            _queue = new int[k];
            _front = 0;
            _size = 0;
        }

        public bool EnQueue(int value)
        {
            if (_size == _capacity) return false;
            int rear = (_front + _size) % _capacity;
            _queue[rear] = value;
            _size++;
            return true;
        }

        public bool DeQueue()
        {
            if (_size == 0) return false;
            _front = (_front + 1) % _capacity;
            _size--;
            return true;
        }

        public int Front()
        {
            if (_size == 0) return -1;
            return _queue[_front];
        }

        public int Rear()
        {
            if (_size == 0) return -1;
            int rear = (_front + _size - 1) % _capacity;
            return _queue[rear];
        }

        public bool IsEmpty()
        {
            return _size == 0;
        }

        public bool IsFull()
        {
            return _size == _capacity;
        }
    }

    public class Program
    {
        static void Main(string[] args)
        {
            MyCircularQueue cq = new MyCircularQueue(3);
            Console.WriteLine(cq.EnQueue(1)); // true
            Console.WriteLine(cq.EnQueue(2)); // true
            Console.WriteLine(cq.EnQueue(3)); // true
            Console.WriteLine(cq.EnQueue(4)); // false
            Console.WriteLine(cq.Rear());     // 3
            Console.WriteLine(cq.IsFull());   // true
            Console.WriteLine(cq.DeQueue());  // true
            Console.WriteLine(cq.EnQueue(4)); // true
            Console.WriteLine(cq.Rear());     // 4
        }
    }
}
