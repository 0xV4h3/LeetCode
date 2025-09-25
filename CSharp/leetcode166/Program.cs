using System.Text;

namespace leetcode166
{
    //166. Fraction to Recurring Decimal
    public class Solution
    {
        public string FractionToDecimal(int numerator, int denominator)
        {
            if (numerator == 0) return "0";
            var result = new StringBuilder();

            bool isNegative = (numerator > 0) ^ (denominator > 0);
            if (isNegative) result.Append("-");

            long dividend = Math.Abs((long)numerator);
            long divisor = Math.Abs((long)denominator);

            result.Append(dividend / divisor);
            dividend %= divisor;

            if (dividend == 0) return result.ToString();

            result.Append(".");

            var remainderToPosition = new Dictionary<long, int>();

            while (dividend != 0)
            {
                remainderToPosition[dividend] = result.Length;
                dividend *= 10;
                result.Append(dividend / divisor);
                dividend %= divisor;

                if (remainderToPosition.ContainsKey(dividend))
                {
                    int index = remainderToPosition[dividend];
                    result.Insert(index, "(");
                    result.Append(")");
                    break;
                }
            }
            return result.ToString();
        }
    }
    class Program
    {
        static void Main(string[] args)
        {
            var sol = new Solution();
            Console.WriteLine(sol.FractionToDecimal(1, 2)); // "0.5"
            Console.WriteLine(sol.FractionToDecimal(2, 1)); // 2
            Console.WriteLine(sol.FractionToDecimal(4, 333)); // "0.(012)"
        }
    }
}
