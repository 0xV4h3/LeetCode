namespace leetcode2169
{
    //2169. Count Operations to Obtain Zero
    public class Solution
    {
        public int CountOperations(int num1, int num2)
        {
            int count = 0;
            while (num1 != 0 && num2 != 0)
            {
                count += num1 / num2;
                num1 %= num2;
                (num1, num2) = (num2, num1);
            }
            return count;
        }
    }

    public class Program
    {
        static void Main(string[] args)
        {
            var sol = new Solution();
            Console.WriteLine(sol.CountOperations(2, 3)); // 3
            Console.WriteLine(sol.CountOperations(10, 10)); // 1
        }
    }
}
