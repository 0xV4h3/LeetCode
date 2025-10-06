namespace leetcode778
{
    //778. Swim in Rising Water
    public class Solution
    {
        public int SwimInWater(int[][] grid)
        {
            int m = grid.Length, n = grid[0].Length;
            int[][] directions = new int[][]
            {
            new int[] {0, 1},
            new int[] {1, 0},
            new int[] {0, -1},
            new int[] {-1, 0}
            };

            int lo = grid[0][0];
            int hi = 0;

            foreach (var row in grid)
            {
                foreach (int val in row)
                    hi = Math.Max(hi, val);
            }

            while (lo < hi)
            {
                int mid = lo + (hi - lo) / 2;
                if (Possible(grid, mid, m, n, directions))
                    hi = mid;
                else
                    lo = mid + 1;
            }

            return lo;
        }

        private bool Possible(int[][] grid, int mid, int m, int n, int[][] directions)
        {
            if (grid[0][0] > mid) return false;
            bool[,] seen = new bool[m, n];
            return Dfs(grid, 0, 0, mid, seen, m, n, directions);
        }

        private bool Dfs(int[][] grid, int r, int c, int mid, bool[,] seen, int m, int n, int[][] directions)
        {
            if (r == m - 1 && c == n - 1)
                return true;

            seen[r, c] = true;

            foreach (var dir in directions)
            {
                int nr = r + dir[0];
                int nc = c + dir[1];

                if (nr >= 0 && nr < m && nc >= 0 && nc < n && !seen[nr, nc])
                {
                    if (grid[nr][nc] <= mid)
                    {
                        if (Dfs(grid, nr, nc, mid, seen, m, n, directions))
                            return true;
                    }
                }
            }

            return false;
        }
    }

    internal class Program
    {
        static void Main(string[] args)
        {
            var sol = new Solution();
            Console.WriteLine(sol.SwimInWater([[0, 2], [1, 3]])); // 3
            Console.WriteLine(sol.SwimInWater([[0, 1, 2, 3, 4], [24, 23, 22, 21, 5], [12, 13, 14, 15, 16], [11, 17, 18, 19, 20], [10, 9, 8, 7, 6]])); // 16
        }
    }
}
