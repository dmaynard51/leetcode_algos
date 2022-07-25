class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height)-1
        
        highestL = height[l]
        highestR = height[r]
        res = 0
        while l < r:
            if highestR < highestL:
                r -= 1
                highestR = max(highestR, height[r])
                res += (highestR - height[r])
            else:
                l += 1
                highestL = max(highestL, height[l])
                res += (highestL - height[l])
            #print res, l, r
        return res
                
            
        