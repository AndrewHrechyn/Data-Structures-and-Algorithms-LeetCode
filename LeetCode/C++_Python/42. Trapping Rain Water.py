class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        tot = 0
        b = [0] * len(height)
        a = [0] * len(height)
        b[0] = height[0]
        a[-1] = height[-1]
        for i in range(1, len(height)):
            b[i] = max(b[i - 1], height[i])
        for i in range(len(height) - 2, -1, -1):
            a[i] = max(a[i + 1], height[i])
        for i in range(1, len(height) - 1):
            if (height[i] < b[i - 1]) and (height[i] < a[i + 1]):
                tot += min(b[i - 1], a[i + 1]) - height[i]
        return tot