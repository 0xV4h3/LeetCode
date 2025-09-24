namespace leetcode1
{
    public class Solution
    {
        public int[] TwoSum(int[] nums, int target)
        {
            var numIdx = new Dictionary<int, int>();
            for (int i = 0; i < nums.Length; i++)
            {
                int complement = target - nums[i];
                if (numIdx.ContainsKey(complement) && numIdx[complement] != i)
                    return new int[] {numIdx[complement], i };
                numIdx[nums[i]] = i;
            }
            return new int[0];
        }
    }

    class Program
    {
        static void Main()
        {
            var sol = new Solution();
            Console.WriteLine(string.Join(",", sol.TwoSum(new[] { 2, 7, 11, 15 }, 9))); // 0,1
            Console.WriteLine(string.Join(",", sol.TwoSum(new[] { 3, 2, 4 }, 6))); // 1,2
            Console.WriteLine(string.Join(",", sol.TwoSum(new[] { 3, 3 }, 6))); // 0,1
        }
    }
}
