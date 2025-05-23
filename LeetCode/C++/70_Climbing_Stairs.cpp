class Solution {
public:
    int climbStairs(int n) {
        vector<int> memo(n + 1, -1);
        return climb_Stairs(0, n, memo);
    }

    int climb_Stairs(int i, int n, vector<int>& memo) {
        if (i > n) return 0;
        if (i == n) return 1;
        if (memo[i] != -1) return memo[i];
        memo[i] = climb_Stairs(i + 1, n, memo) + climb_Stairs(i + 2, n, memo);
        return memo[i];
    }
};