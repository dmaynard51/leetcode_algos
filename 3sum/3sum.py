class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()

        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            l = i + 1
            r = len(nums)-1
            sm = 0
            while l < r:
                sm = nums[i] + nums[l] + nums[r]
                if sm == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    
                    while l < r and nums[l] == nums[l+1]:
                        l+=1
                    
                    while l < r and nums[r] == nums[r-1]:
                        r -=1
                if sm < 0:
                    l+=1
                elif sm > 0:
                    r -=1
                else:
                    r -=1
                    l+=1
        return res