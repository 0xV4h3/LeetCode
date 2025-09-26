namespace leetcode611
{
    //611. Valid Triangle Number
    public class Solution
    {
        public int TriangleNumber(int[] nums)
        {
            Array.Sort(nums);
            int n = nums.Length;
            int triangles = 0;

            for (int i = n - 1; i >= 2; i--)
            {
                int left = 0, right = i - 1;
                while (left < right)
                {
                    if (nums[left] + nums[right] > nums[i])
                    {
                        triangles += right - left;
                        right--;
                    }
                    else
                    {
                        left++;
                    }
                }
            }
            return triangles;
        }
    }

    internal class Program
    {
        static void Main(string[] args)
        {
            var sol = new Solution();
            Console.WriteLine(sol.TriangleNumber([2, 2, 3, 4])); // 3
            Console.WriteLine(sol.TriangleNumber([4, 2, 3, 4])); // 4
        }
    }
}
