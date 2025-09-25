#include <iostream>
#include <vector>

//120. Triangle
class Solution {
public:
    int minimumTotal(std::vector<std::vector<int>>& triangle) {
        for (int i = triangle.size() - 2; i >= 0; i--)
            for (int j = 0; j < triangle[i].size(); j++)
                triangle[i][j] += std::min(triangle[i + 1][j], triangle[i + 1][j + 1]);
        return triangle[0][0];
    }
};

int main() {
    Solution sol;
    std::vector<std::vector<int>> triangle1 = {{2},{3,4},{6,5,7},{4,1,8,3}};
    std::cout << sol.minimumTotal(triangle1) << std::endl; // 11
    std::vector<std::vector<int>> triangle2 = {{-10}};
    std::cout << sol.minimumTotal(triangle2) << std::endl; // -10
}