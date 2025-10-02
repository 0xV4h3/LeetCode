namespace leetcode3100
{
    internal class Program
    {
        //3100. Water Bottles II
        public class Solution
        {
            public int MaxBottlesDrunk(int numBottles, int numExchange)
            {
                int maxDrunk = numBottles;
                while (numBottles >= numExchange)
                {
                    numBottles -= numExchange - 1;
                    numExchange++;
                    maxDrunk++;
                }
                return maxDrunk;
            }
        }

        static void Main(string[] args)
        {
            var sol = new Solution();
            Console.WriteLine(sol.MaxBottlesDrunk(numBottles: 13, numExchange: 6)); // 15
            Console.WriteLine(sol.MaxBottlesDrunk(numBottles: 10, numExchange: 3)); // 13
        }
    }
}
