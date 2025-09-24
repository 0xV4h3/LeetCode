# 217. Contains Duplicate
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        count = {}
        for number in nums:
            if number in count:
                count[number] += 1
                if count[number] == 2:
                    return True
            else:
                count[number] = 1
        return False

if __name__ == "__main__":
    sol = Solution()
    example1 = sol.containsDuplicate([1,2,3,1])
    print(example1)
    example2 = sol.containsDuplicate([1,2,3,4])
    print(example2)
    example3 = sol.containsDuplicate([1,1,1,3,3,4,3,2,4,2])
    print(example3)