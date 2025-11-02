namespace leetcode303
{
    //303. Range Sum Query - Immutable

    // 1 version
    //public class NumArray
    //{
    //    private int[] _nums;
    //    public NumArray(int[] nums)
    //    {
    //        _nums = nums;
    //    }

    //    public int SumRange(int left, int right)
    //    {
    //        int sum = 0;
    //        for (int i = left; i <= right; i++) sum += _nums[i];
    //        return sum;
    //    }
    //}

    // 2 version - prefix sum
    public class NumArray
    {
        private int[] _sums;
        public NumArray(int[] nums)
        {
            _sums = new int[nums.Length + 1];
            _sums[0] = 0;
            for (int i = 0; i < nums.Length; i++)
                _sums[i + 1] = nums[i] + _sums[i];

        }

        public int SumRange(int left, int right)
        {
            return _sums[right + 1] - _sums[left];
        }
    }

    public class Program
    {
        static void Main(string[] args)
        {
            NumArray numArray = new([-2, 0, 3, -5, 2, -1]);
            Console.WriteLine(numArray.SumRange(0, 2)); // 1
            Console.WriteLine(numArray.SumRange(2, 5)); // -1
            Console.WriteLine(numArray.SumRange(0, 5)); // -3
        }
    }
}
