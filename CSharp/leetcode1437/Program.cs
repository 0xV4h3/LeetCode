namespace leetcode1437
{
    //1437. Check If All 1's Are at Least Length K Places Away
    public class Solution
    {
        public bool KLengthApart(int[] nums, int k)
        {
            int lastOneIndex = -1;
            for (int i = 0; i < nums.Length; i++)
            {
                if (nums[i] == 1)
                {
                    if (lastOneIndex != -1 && i - lastOneIndex - 1 < k)
                    {
                        return false;
                    }
                    lastOneIndex = i;
                }
            }
            return true;
        }
    }

    public class Program
    {
        static void Main(string[] args)
        {
            var sol = new Solution();
            Console.WriteLine(sol.KLengthApart([1, 0, 0, 0, 1, 0, 0, 1], 2)); // True
            Console.WriteLine(sol.KLengthApart([1, 0, 0, 1, 0, 1], 2)); // False
        }
    }
}
