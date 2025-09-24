# 27. Remove Element
from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k

if __name__ == "__main__":
    sol = Solution()
    nums1 = [3,2,2,3]
    k1 = sol.removeElement(nums1, 3)
    print(k1, nums1[:k1])  # 2, [2,2]

    nums2 = [0,1,2,2,3,0,4,2]
    k2 = sol.removeElement(nums2, 2)
    print(k2, nums2[:k2])  # 5, [0,1,3,0,4]
