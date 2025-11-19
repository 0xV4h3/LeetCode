namespace leetcode2154
{
    //2154. Keep Multiplying Found Values by Two
    public class Solution
    {
        // SortedSet version - slow
        //public int FindFinalValue(int[] nums, int original)
        //{
        //    SortedSet<int> numbers = new();
        //    bool originalFound = false;
        //    foreach (var num in nums)
        //    {
        //        if (num == original)
        //        {
        //            originalFound = true;
        //        }
        //        numbers.Add(num);
        //    }
        //    if (!originalFound)
        //    {
        //        return original;
        //    }
        //    while (numbers.Contains(original))
        //    {
        //        original *= 2;
        //    }
        //    return original;
        //}

        // HashSet version - fast
        public int FindFinalValue(int[] nums, int original)
        {
            HashSet<int> numbers = new(nums);
            while(numbers.Contains(original))
            {
                original *= 2;
            }
            return original;
        }
    }

    public class Program
    {
        static void Main(string[] args)
        {
            var sol = new Solution();
            Console.WriteLine(sol.FindFinalValue([5, 3, 6, 1, 12], 3)); // 24
            Console.WriteLine(sol.FindFinalValue([2, 7, 9], 4)); // 4
        }
    }
}
