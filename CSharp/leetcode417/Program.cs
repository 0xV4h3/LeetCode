namespace leetcode417
{
    //417. Pacific Atlantic Water Flow
    public class Solution
    {
        private int m, n;
        private int[][] directions = new int[][]
        {
            new int[] {1, 0},
            new int[] {-1, 0},
            new int[] {0, 1},
            new int[] {0, -1}
        };

        public IList<IList<int>> PacificAtlantic(int[][] heights)
        {
            m = heights.Length;
            n = heights[0].Length;

            bool[,] pacific = new bool[m, n];
            bool[,] atlantic = new bool[m, n];

            for (int j = 0; j < n; j++) dfs(0, j, heights, pacific);
            for (int i = 0; i < m; i++) dfs(i, 0, heights, pacific);

            for (int j = 0; j < n; j++) dfs(m - 1, j, heights, atlantic);
            for (int i = 0; i < m; i++) dfs(i, n - 1, heights, atlantic);

            var result = new List<IList<int>>();
            for (int i = 0; i < m; i++)
            {
                for (int j = 0; j < n; j++)
                {
                    if (pacific[i, j] && atlantic[i, j])
                    {
                        result.Add(new List<int> { i, j });
                    }
                }
            }

            return result;
        }

        private void dfs(int i, int j, int[][] heights, bool[,] visited)
        {
            if (visited[i, j]) return;
            visited[i, j] = true;

            foreach (var d in directions)
            {
                int x = i + d[0], y = j + d[1];
                if (x < 0 || x >= m || y < 0 || y >= n) continue;
                if (heights[x][y] < heights[i][j]) continue;
                dfs(x, y, heights, visited);
            }
        }
    }

    internal class Program
    {
        static void Main(string[] args)
        {
            var sol = new Solution();

            int[][] heights1 = new int[][]
            {
                new int[] {1, 2, 2, 3, 5},
                new int[] {3, 2, 3, 4, 4},
                new int[] {2, 4, 5, 3, 1},
                new int[] {6, 7, 1, 4, 5},
                new int[] {5, 1, 1, 2, 4}
            };

            var result1 = sol.PacificAtlantic(heights1);
            foreach (var list in result1)
            {
                Console.Write($"[{list[0]}, {list[1]}] ");
            } // [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
            Console.WriteLine();

            int[][] heights2 = new int[][]
            {
                new int[] {1}
            };

            var result2 = sol.PacificAtlantic(heights2);
            foreach (var list in result2)
            {
                Console.Write($"[{list[0]}, {list[1]}] ");
            } // [[0,0]]
            Console.WriteLine();
        }
    }
}
