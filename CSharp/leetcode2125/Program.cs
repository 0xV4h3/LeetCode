namespace leetcode2125
{
    //2125. Number of Laser Beams in a Bank
    public class Solution
    {
        public int NumberOfBeams(string[] bank)
        {
            int laserBeams = 0, prev = 0;

            foreach (string row in bank)
            {
                int device = row.Count(cell  => cell == '1');
                if (device > 0)
                {
                    laserBeams += device * prev;
                    prev = device;
                }
            }
            return laserBeams;
        }
    }

    public class Program
    {
        static void Main(string[] args)
        {
            var sol = new Solution();
            Console.WriteLine(sol.NumberOfBeams(bank : ["011001", "000000", "010100", "001000"])); // 8
            Console.WriteLine(sol.NumberOfBeams(bank : ["000", "111", "000"])); // 0
        }
    }
}
