using System.Collections.Generic;

namespace leetcode3370
{
    //3370. Smallest Number With All Set Bits
    public class Solution
    {
        public int SmallestNumber(int n)
        {
            return (int)Math.Pow(2, (int)Math.Log2(n) + 1) - 1;
        }
    }

    public class Program
    {
        static void Main(string[] args)
        {
            var sol = new Solution();
            Console.WriteLine(sol.SmallestNumber(n: 5)); // 7
            Console.WriteLine(sol.SmallestNumber(n: 10)); // 15
            Console.WriteLine(sol.SmallestNumber(n: 3)); // 3
        }
    }
}
