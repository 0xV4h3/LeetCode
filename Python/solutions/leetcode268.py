# 268. Missing Number
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        num_sum = ((len(nums) + 1) / 2) * len(nums)
        return int(num_sum - sum(nums))

if __name__ == "__main__":
    sol = Solution()
    example1 = sol.missingNumber(nums = [3,0,1])
    print(example1)
    example2 = sol.missingNumber(nums = [0,1])
    print(example2)
    example3 = sol.missingNumber(nums = [9,6,4,2,3,5,7,0,1])
    print(example3)