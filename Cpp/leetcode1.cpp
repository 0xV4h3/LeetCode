#include <iostream>
#include <vector>
#include <unordered_map>

class Solution {
public:
    std::vector<int> twoSum(std::vector<int>& nums, int target) {
        std::unordered_map<int, int> numIdx;
        for (int i = 0; i < nums.size(); ++i) {
            int complement = target - nums[i];
            if (numIdx.contains(complement) && numIdx[complement] != i)
                return {numIdx[complement], i};
            numIdx[nums[i]] = i;
        }
        return {};
    }
};

int main() {
    Solution sol;
    std::vector<int> nums1 = {2,7,11,15};
    std::vector<int> res1 = sol.twoSum(nums1, 9); // [0,1]
    std::cout << res1[0] << "," << res1[1] << std::endl;
    std::vector<int> nums2 = {3,2,4};
    std::vector<int> res2 = sol.twoSum(nums2, 6); // [1,2]
    std::cout << res2[0] << "," << res2[1] << std::endl;
    std::vector<int> nums3 = {3,3};
    std::vector<int> res3 = sol.twoSum(nums3, 6); // [0,1]
    std::cout << res3[0] << "," << res3[1] << std::endl;
}