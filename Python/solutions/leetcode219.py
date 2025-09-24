# 219. Contains Duplicate II
class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        count = {}
        i = 0
        for number in nums:
            if number in count:
                if abs(count[number] - i) <= k:
                    return True
                else:
                    count[number] = i
            else:
                count[number] = i
            i += 1
        return False

if __name__ == "__main__":
    sol = Solution()
    example1 = sol.containsNearbyDuplicate(nums = [1,2,3,1], k = 3)
    print(example1)
    example2 = sol.containsNearbyDuplicate(nums = [1,0,1,1], k = 1)
    print(example2)
    example3 = sol.containsNearbyDuplicate(nums = [1,2,3,1,2,3], k = 2)
    print(example3)