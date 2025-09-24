# 349. Intersection of Two Arrays
class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        return list(set(nums1).intersection(set(nums2)))

if __name__ == "__main__":
    sol = Solution()
    example1 = sol.intersection(nums1 = [1,2,2,1], nums2 = [2,2])
    print(example1)
    example2 = sol.intersection(nums1 = [4,9,5], nums2 = [9,4,9,8,4])
    print(example2)
