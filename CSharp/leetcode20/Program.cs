namespace leetcode20
{
    //20. Valid Parentheses
    public class Solution
    {
        public bool IsValid(string s)
        {
            Stack<char> stack = new();

            for (int i = 0; i < s.Length; ++i)
            {
                if (s[i] == '(' || s[i] == '{' || s[i] == '[')
                    stack.Push(s[i]);
                else
                {
                    if (stack.Count == 0) return false;

                    char lastOpening = stack.Pop();
                    if ((lastOpening == '(' && s[i] != ')') ||
                       (lastOpening == '{' && s[i] != '}') ||
                       (lastOpening == '[' && s[i] != ']'))
                        return false;
                }
            }

            return stack.Count == 0;
        }
    }

    public class Program
    {
        static void Main(string[] args)
        {
            var sol = new Solution();
            Console.WriteLine(sol.IsValid("()")); // true
            Console.WriteLine(sol.IsValid("()[]{}")); // true
            Console.WriteLine(sol.IsValid("(]")); // false
            Console.WriteLine(sol.IsValid("([])")); // true
            Console.WriteLine(sol.IsValid("([)]")); // false
        }
    }
}
