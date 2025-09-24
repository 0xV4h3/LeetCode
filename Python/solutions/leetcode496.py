# 496. Next Greater Element I
class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        stack = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    if j == len(nums2) - 1:
                        stack.append(-1)
                    else:
                        for k in range(j, len(nums2)):
                            if nums2[k] > nums2[j]:
                                stack.append(nums2[k])
                                break
                        else:
                            stack.append(-1)
                    break
        return stack

if __name__ == "__main__":
    sol = Solution()
    example1 = sol.nextGreaterElement([4,1,2], [1,3,4,2])
    print(example1)
    example2 = sol.nextGreaterElement([2,4], [1,2,3,4])
    print(example2)


