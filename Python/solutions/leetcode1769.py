# 1769. Minimum Number of Operations to Move All Balls to Each Box
from typing import List

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        operations = [0] * len(boxes)
        for box in range(len(boxes)):
            if boxes[box] == '1':
                for other_box in range(len(boxes)):
                    operations[other_box] += abs(other_box - box)

        return operations

if __name__ == "__main__":
    sol = Solution()
    print(sol.minOperations(boxes = "110"))  # [1,1,3]
    print(sol.minOperations(boxes = "001011"))  # [11,8,5,4,3,4]

