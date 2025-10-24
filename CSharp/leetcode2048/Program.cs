using static System.Net.Mime.MediaTypeNames;

namespace leetcode2048
{
    //2048. Next Greater Numerically Balanced Number
    public class Solution
    {
        public int NextBeautifulNumber(int n)
        {
            for (int i = n + 1; i <= 1224444; i++)
            {
                if(isBalanced(i)) return i;
            }
            return -1;
        }

        public bool isBalanced(int n)
        {
            int[] digitOccurrences = new int[10];
            while (n > 0)
            {
                digitOccurrences[n % 10]++;
                n /= 10;
            }
            for (int i = 0; i < 10; i++)
            {
                if (digitOccurrences[i] > 0 & digitOccurrences[i] != i) return false; 
            }
            return true;
        }
    }
    public class Program
    {
        static void Main(string[] args)
        {
            var sol = new Solution();
            Console.WriteLine(sol.NextBeautifulNumber(n: 1)); // 22
            Console.WriteLine(sol.NextBeautifulNumber(n: 1000)); // 1333
            Console.WriteLine(sol.NextBeautifulNumber(n: 3000)); // 3133
            Console.WriteLine(sol.NextBeautifulNumber(n: 748601)); // 1224444
        }
    }
}
