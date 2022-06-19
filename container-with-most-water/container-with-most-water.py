class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        
        l = 0
        r = len(height)-1
        curr = 0
        res = 0
        while l < r:
            if height[l] < height[r]:
                curr = max(curr,height[l] * (r-l))
                l += 1
            else:
                curr = max(curr, height[r] * (r-l))
                r -=1
            res = max(curr, res)
        return res