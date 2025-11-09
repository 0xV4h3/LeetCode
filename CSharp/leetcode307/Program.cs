namespace leetcode307
{
    //307. Range Sum Query - Mutable

    // Prefix Sum - doesn't work
    //public class NumArray
    //{
    //    private List<int> _prefixSum = [];
    //    public NumArray(int[] nums)
    //    {
    //        int temp = 0;
    //        _prefixSum.Add(0);
    //        foreach (int num in nums)
    //        {
    //            temp += num;
    //            _prefixSum.Add(temp);
    //        }
    //    }

    //    public void Update(int index, int val)
    //    {
    //        int temp = val - (_prefixSum[index + 1] - _prefixSum[index]);
    //        for (int i = index + 1; i < _prefixSum.Count; i++)
    //        {
    //            _prefixSum[i] += temp;
    //        }
    //    }

    //    public int SumRange(int left, int right)
    //    {
    //        return _prefixSum[right + 1] - _prefixSum[left];
    //    }
    //}

    // Segment Tree
    public class SegmentTree
    {
        private int[] tree;
        private int n;

        public SegmentTree(int[] nums)
        {
            n = nums.Length;
            tree = new int[4 * n];
            BuildTree(nums, 0, n - 1, 0);
        }

        private void BuildTree(int[] nums, int left, int right, int index)
        {
            if (left == right)
            {
                tree[index] = nums[left];
                return;
            }

            int mid = (left + right) / 2;
            BuildTree(nums, left, mid, 2 * index + 1);
            BuildTree(nums, mid + 1, right, 2 * index + 2);
            tree[index] = tree[2 * index + 1] + tree[2 * index + 2];
        }

        public int SumRange(int left, int right, int index, int qleft, int qright)
        {
            if (qright < left || qleft > right)
                return 0;

            if (qleft <= left && right <= qright)
                return tree[index];

            int mid = (left + right) / 2;
            return SumRange(left, mid, 2 * index + 1, qleft, qright) +
                   SumRange(mid + 1, right, 2 * index + 2, qleft, qright);
        }

        public void Update(int left, int right, int index, int pos, int val)
        {
            if (left == right)
            {
                tree[index] = val;
                return;
            }

            int mid = (left + right) / 2;
            if (pos <= mid)
                Update(left, mid, 2 * index + 1, pos, val);
            else
                Update(mid + 1, right, 2 * index + 2, pos, val);

            tree[index] = tree[2 * index + 1] + tree[2 * index + 2];
        }

        public int Size => n;
    }

    public class NumArray
    {
        private SegmentTree segTree;

        public NumArray(int[] nums)
        {
            segTree = new SegmentTree(nums);
        }

        public void Update(int index, int val)
        {
            segTree.Update(0, segTree.Size - 1, 0, index, val);
        }

        public int SumRange(int left, int right)
        {
            return segTree.SumRange(0, segTree.Size - 1, 0, left, right);
        }
    }

    public class Program
    {
        static void Main(string[] args)
        {
            NumArray numArray = new([1, 3, 5]);
            Console.WriteLine(numArray.SumRange(0, 2)); // 9
            numArray.Update(1, 2);
            Console.WriteLine(numArray.SumRange(0, 2)); // 8

            NumArray numArray1 = new([-1]);
            Console.WriteLine(numArray1.SumRange(0, 0)); // -1
            numArray1.Update(0, 1);
            Console.WriteLine(numArray1.SumRange(0, 0)); // 1
        }
    }
}
