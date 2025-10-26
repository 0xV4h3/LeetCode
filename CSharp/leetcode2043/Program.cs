namespace leetcode2043
{
    //2043. Simple Bank System
    public class Bank
    {
        private long[] _balance;
        private readonly int _accounts;
        public Bank(long[] balance)
        {
            _balance = balance;
            _accounts = balance.Length;
        }

        public bool Transfer(int account1, int account2, long money)
        {
            if (account1 > _accounts || account2 > _accounts) return false;
            if (_balance[account1 - 1] < money) return false;
            _balance[account1 - 1] -= money;
            _balance[account2 - 1] += money;
            return true;
        }

        public bool Deposit(int account, long money)
        {
            if (account > _accounts) return false;
            _balance[account - 1] += money;
            return true;
        }

        public bool Withdraw(int account, long money)
        {
            if (account > _accounts) return false;
            if (_balance[account - 1] < money) return false;
            _balance[account - 1] -= money;
            return true;
        }
    }

    public class Program
    {
        static void Main(string[] args)
        {
            Bank bank = new Bank([10, 100, 20, 50, 30]);
            Console.WriteLine(bank.Withdraw(3, 10)); // true
            Console.WriteLine(bank.Transfer(5, 1, 20)); // true
            Console.WriteLine(bank.Deposit(5, 20)); // true
            Console.WriteLine(bank.Transfer(3, 4, 15)); // false
            Console.WriteLine(bank.Withdraw(10, 50)); // false
        }
    }
}
