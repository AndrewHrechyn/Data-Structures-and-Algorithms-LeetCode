class Solution {
public:
    int trap(vector<int>& height) {
        int n = height.size();
        if (n == 0) return 0;

        int total = 0;
        vector<int> leftMax(n, 0);
        vector<int> rightMax(n, 0);

        // Заповнення масиву максимумів зліва
        leftMax[0] = height[0];
        for (int i = 1; i < n; i++) {
            leftMax[i] = max(leftMax[i - 1], height[i]);
        }

        // Заповнення масиву максимумів справа
        rightMax[n - 1] = height[n - 1];
        for (int i = n - 2; i >= 0; i--) {
            rightMax[i] = max(rightMax[i + 1], height[i]);
        }

        // Підрахунок загальної кількості зібраної води
        for (int i = 1; i < n - 1; i++) {
            if (height[i] < leftMax[i - 1] && height[i] < rightMax[i + 1]) {
                total += min(leftMax[i - 1], rightMax[i + 1]) - height[i];
            }
        }

        return total;
    }
};