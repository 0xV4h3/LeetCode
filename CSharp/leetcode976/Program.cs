namespace leetcode976
{
    //976. Largest Perimeter Triangle
    public class Solution
    {
        public int LargestPerimeter(int[] nums)
        {
            Array.Sort(nums);
            for (int i = nums.Length - 1; i >= 2; i--)
            {
                if (nums[i - 2] + nums[i - 1] > nums[i])
                {
                    return nums[i - 2] + nums[i - 1] + nums[i];
                }
            }
            return 0;
        }
    }

    internal class Program
    {
        static void Main(string[] args)
        {
            var sol = new Solution();
            Console.WriteLine(sol.LargestPerimeter([2, 1, 2])); // 5
            Console.WriteLine(sol.LargestPerimeter([1, 2, 1, 10])); // 0
        }
    }
}
