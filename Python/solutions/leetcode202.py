# 202. Happy Number
class Solution:
    def isHappy(self, n: int) -> bool:
        not_happy = True
        while not_happy:
            squares_sum = 0
            for digit in str(n):
                squares_sum += int(digit) * int(digit)
            if squares_sum < 10:
                if squares_sum == 1 or squares_sum == 7:
                    not_happy = False
                else:
                    break
            else:
                n = squares_sum
        return not not_happy

if __name__ == "__main__":
    sol = Solution()
    example1 = sol.isHappy(19)
    print(example1)
    example2 = sol.isHappy(2)
    print(example2)
    example3 = sol.isHappy(1111111)
    print(example3)