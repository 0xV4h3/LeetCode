namespace leetcode2221
{
    //2221. Find Triangular Sum of an Array
    public class Solution
    {
        public int TriangularSum(int[] nums)
        {
            int[] newNums = (int[])nums.Clone();
            int length = newNums.Length;

            while (length != 1)
            {
                for (int i = 0; i < length - 1; i++)
                {
                    newNums[i] = (newNums[i] + newNums[i + 1]) % 10;
                }
                length--;
            }
            return newNums[0];
        }
    }

    internal class Program
    {
        static void Main(string[] args)
        {
            var sol = new Solution();
            Console.WriteLine(sol.TriangularSum([1, 2, 3, 4, 5])); // 8
            Console.WriteLine(sol.TriangularSum([5])); // 5
        }
    }
}
