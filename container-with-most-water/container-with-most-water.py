class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height)-1
        res = 0
        while l < r:
            if height[l] < height[r]:
                res = max(res, height[l] * (r- l))
                l += 1
            else:
                res = max(res, height[r] * (r - l))
                r -= 1
                
        return res