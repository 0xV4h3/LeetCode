# 88. Merge Sorted Array
from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1 = m - 1
        p2 = n - 1
        right = m + n - 1

        while p2 >= 0:
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[right] = nums1[p1]
                p1 -= 1
            else:
                nums1[right] = nums2[p2]
                p2 -= 1

            right -= 1

if __name__ == "__main__":
    sol = Solution()
    nums1 = [1, 2, 3, 0, 0, 0]
    sol.merge(nums1, m=3, nums2=[2, 5, 6], n=3)
    print(nums1)  # [1,2,2,3,5,6]
    nums1 = [1]
    sol.merge(nums1, m=1, nums2=[], n=0)
    print(nums1)  # [1]
    nums1 = [0]
    sol.merge(nums1, m=0, nums2=[1], n=1)
    print(nums1)  # [1]
