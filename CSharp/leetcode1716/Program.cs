namespace leetcode1716
{
    //1716. Calculate Money in Leetcode Bank
    public class Solution
    {
        public int TotalMoney(int n)
        {
            int totalMoney = 0;
            int week = 1;
            while (n > 0)
            {
                int days = n >= 7 ? 7 : n;
                totalMoney += (days * (2 * week + (days - 1))) / 2;
                n -= days;
                week++;
            }
            return totalMoney;
        }
    }

    public class Program
    {
        static void Main(string[] args)
        {
            var sol = new Solution();
            Console.WriteLine(sol.TotalMoney(n: 4)); // 10
            Console.WriteLine(sol.TotalMoney(n: 10)); // 37
            Console.WriteLine(sol.TotalMoney(n: 20)); // 96
        }
    }
}
