namespace leetcode11
{
    //11. Container With Most Water
    public class Solution
    {
        public int MaxArea(int[] height)
        {
            int left = 0, right = height.Length - 1;
            int maxArea = 0;

            while (left < right)
            {
                int currArea = (right - left) * Math.Min(height[left], height[right]);
                maxArea = Math.Max(maxArea, currArea);

                if (height[left] < height[right])
                    left += 1;
                else
                    right -= 1;
            }

            return maxArea;
        }
    }

    internal class Program
    {
        static void Main(string[] args)
        {
            var sol = new Solution();
            Console.WriteLine(sol.MaxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])); // 49
            Console.WriteLine(sol.MaxArea([1, 1])); // 1
        }
    }
}
