class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        
        l = 0
        r = len(height)-1
        leftMost = height[l]
        rightMost = height[r]
        
        while l < r:
            if leftMost < rightMost:
                l += 1
                leftMost = max(leftMost, height[l])
                res += leftMost - height[l]
            else:
                r -= 1
                rightMost = max(rightMost, height[r])
                res += rightMost - height[r]
        return res