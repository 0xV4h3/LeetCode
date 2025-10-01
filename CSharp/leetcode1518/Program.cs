namespace leetcode1518
{
    //1518. Water Bottles
    public class Solution
    {
        public int NumWaterBottles(int numBottles, int numExchange)
        {
            return numBottles + (numBottles - 1) / (numExchange-1);
        }
    }

    internal class Program
    {
        static void Main(string[] args)
        {
            var sol = new Solution();
            Console.WriteLine(sol.NumWaterBottles(numBottles:9, numExchange:3)); // 13
            Console.WriteLine(sol.NumWaterBottles(numBottles:15, numExchange:4)); // 19
        }
    }
}
