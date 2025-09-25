namespace leetcode120
{
    //120. Triangle
    public class Solution
    {
        public int MinimumTotal(IList<IList<int>> triangle)
        {
            for (int i = triangle.Count - 2; i >= 0; i--)
                for (int j = 0; j < triangle[i].Count; j++)
                    triangle[i][j] += Math.Min(triangle[i + 1][j], triangle[i + 1][j + 1]);
            return triangle[0][0];
        }
    }

    internal class Program
    {
        static void Main(string[] args)
        {
            var sol = new Solution();
            Console.WriteLine(sol.MinimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]])); // 11
            Console.WriteLine(sol.MinimumTotal([[-10]])); // -10
        }
    }
}
