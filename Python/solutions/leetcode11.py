class Solution:
    def maxArea(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0
        while left < right:
            current_area = (right - left) * min(height[left], height[right])
            max_area = max(max_area, current_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area

sol = Solution()
case1 = sol.maxArea([1,8,6,2,5,4,8,3,7])
print(f"Max area in 1 case : {case1}")
case2 = sol.maxArea([1,1])
print(f"Max area in 2 case: {case2}")