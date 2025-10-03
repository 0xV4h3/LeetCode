namespace leetcode407
{
    //407. Trapping Rain Water II
    public class Solution
    {
        public int TrapRainWater(int[][] height)
        {
            int m = height.Length;
            int n = height[0].Length;

            var pq = new PriorityQueue<(int h, int r, int c), int>();
            bool[,] vis = new bool[m, n];

            for (int i = 0; i < m; i++)
            {
                for (int j = 0; j < n; j++)
                {
                    if (i == 0 || i == m - 1 || j == 0 || j == n - 1)
                    {
                        pq.Enqueue((height[i][j], i, j), height[i][j]);
                        vis[i, j] = true;
                    }
                }
            }

            int[][] dir = new int[][]
            {
            new int[]{0, 1}, new int[]{0, -1},
            new int[]{1, 0}, new int[]{-1, 0}
            };

            int water = 0;

            while (pq.Count > 0)
            {
                var (ht, r, c) = pq.Dequeue();

                foreach (var d in dir)
                {
                    int nr = r + d[0], nc = c + d[1];

                    if (nr >= 0 && nc >= 0 && nr < m && nc < n && !vis[nr, nc])
                    {
                        vis[nr, nc] = true;

                        if (height[nr][nc] < ht)
                            water += ht - height[nr][nc];

                        int newHeight = Math.Max(ht, height[nr][nc]);
                        pq.Enqueue((newHeight, nr, nc), newHeight);
                    }
                }
            }

            return water;
        }
    }

    internal class Program
    {
        static void Main(string[] args)
        {
            var sol = new Solution();
            Console.WriteLine(sol.TrapRainWater([[1, 4, 3, 1, 3, 2], [3, 2, 1, 3, 2, 4], [2, 3, 3, 2, 3, 1]])); // 4
            Console.WriteLine(sol.TrapRainWater([[3, 3, 3, 3, 3], [3, 2, 2, 2, 3], [3, 2, 1, 2, 3], [3, 2, 2, 2, 3], [3, 3, 3, 3, 3]])); // 10
        }
    }
}
