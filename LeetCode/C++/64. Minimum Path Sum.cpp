#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        vector<vector<int>> dp(m, vector<int>(n, 0));
        
        for (int i = m - 1; i >= 0; i--) {
            for (int j = n - 1; j >= 0; j--) {
                if (i == m - 1 && j != n - 1)
                    dp[i][j] = grid[i][j] + dp[i][j + 1];
                else if (j == n - 1 && i != m - 1)
                    dp[i][j] = grid[i][j] + dp[i + 1][j];
                else if (j != n - 1 && i != m - 1)
                    dp[i][j] = grid[i][j] + min(dp[i + 1][j], dp[i][j + 1]);
                else
                    dp[i][j] = grid[i][j];
            }
        }
        return dp[0][0];
    }
};

int main() {
    vector<vector<int>> grid; 
    
    grid = {{1,3,1},
            {1,5,1},
            {4,2,1}};

    Solution solution;
    cout << "Minimum Path Sum: " << solution.minPathSum(grid) << endl;

    return 0;
}
