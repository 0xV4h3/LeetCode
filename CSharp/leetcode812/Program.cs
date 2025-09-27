namespace leetcode812
{
    //812. Largest Triangle Area
    public class Solution
    {
        public double LargestTriangleArea(int[][] points)
        {
            int n = points.Length;
            double maxArea = 0;
            for (int i = 0; i < n - 2; i++)
            {
                for (int j = i + 1; j < n - 1; j++)
                {
                    for (int k = j + 1; k < n; k++)
                    {
                        maxArea = Math.Max(maxArea, (0.5 * Math.Abs(points[i][0] * (points[j][1] - points[k][1]) + points[j][0] * (points[k][1] - points[i][1]) + points[k][0] * (points[i][1] - points[j][1]))));
                    }
                }
            }
            return maxArea;
        }
    }

    internal class Program
    {
        static void Main(string[] args)
        {
            var sol = new Solution();
            Console.WriteLine(sol.LargestTriangleArea([[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]])); // 2.00000
            Console.WriteLine(sol.LargestTriangleArea([[1, 0], [0, 0], [0, 1]])); // 0.50000
        }
    }
}
