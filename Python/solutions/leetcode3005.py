# 3005. Count Elements With Maximum Frequency
from collections import defaultdict
from typing import List

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        total_frequency = 0
        max_frequency = 0
        freq_map = defaultdict(int)
        for num in nums:
            freq_map[num] += 1
            max_frequency = max(max_frequency, freq_map[num])

        for num in freq_map:
            if freq_map[num] == max_frequency:
                total_frequency += freq_map[num]

        return total_frequency

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxFrequencyElements(nums = [1,2,2,3,1,4])) # 4
    print(sol.maxFrequencyElements(nums = [1,2,3,4,5])) # 5