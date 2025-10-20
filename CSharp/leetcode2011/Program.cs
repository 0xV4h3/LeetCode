namespace leetcode2011
{
    //2011. Final Value of Variable After Performing Operations
    public class Solution
    {
        public int FinalValueAfterOperations(string[] operations)
        {
            int x = 0;
            foreach (string operation in operations)
            {
                if (operation == "X++" || operation == "++X") x++;
                else x--;
            }
            return x;
        }
    }

    internal class Program
    {
        static void Main(string[] args)
        {
            var sol = new Solution();
            Console.WriteLine(sol.FinalValueAfterOperations(["--X", "X++", "X++"])); // 1
            Console.WriteLine(sol.FinalValueAfterOperations(["++X", "++X", "X++"])); // 3
            Console.WriteLine(sol.FinalValueAfterOperations(["X++", "++X", "--X", "X--"])); // 0
        }
    }
}
