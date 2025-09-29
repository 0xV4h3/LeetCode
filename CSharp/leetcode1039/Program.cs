namespace leetcode1039
{
    //1039. Minimum Score Triangulation of Polygon
    public class Solution
    {
        public int[,] dp = new int[50, 50];
        public int MinScoreTriangulation(int[] values, int i = 0, int j = 0, int result = 0)
        {
            if (j == 0) j = values.Length - 1;
            if (dp[i, j] != 0) return dp[i, j];
            for (int k = i + 1; k < j; k++)
            {
                result = Math.Min(result == 0 ? int.MaxValue : result,
                    MinScoreTriangulation(values, i, k, 0) +
                    values[i] * values[k] * values[j] +
                    MinScoreTriangulation(values, k, j, 0));
            }

            return dp[i, j] = result;
        }
    }

    internal class Program
    {
        static void Main(string[] args)
        {
            var sol1 = new Solution();
            Console.WriteLine(sol1.MinScoreTriangulation([1, 2, 3])); // 6
            var sol2 = new Solution();
            Console.WriteLine(sol2.MinScoreTriangulation([3, 7, 4, 5])); // 144
            var sol3 = new Solution();
            Console.WriteLine(sol3.MinScoreTriangulation([1, 3, 1, 4, 1, 5])); // 13
        }
    }
}
