# 169. Majority Element
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count = dict.fromkeys(nums, 0)
        for number in nums:
            count[number] += 1
            if count[number] > len(nums) / 2:
                return number
        return 0


if __name__ == "__main__":
    sol = Solution()
    example1 = sol.majorityElement([3,2,3])
    print(example1)
    example2 = sol.majorityElement([2,2,1,1,1,2,2])
    print(example2)