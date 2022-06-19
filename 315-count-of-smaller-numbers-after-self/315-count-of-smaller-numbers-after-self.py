from sortedcontainers import SortedList

class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        ans = [0 for i in range(len(nums))]
        sortedList = SortedList()
        
        for i in range(len(nums)-1, -1, -1):
            index = sortedList.bisect_left(nums[i])
            
            ans[i] = index
            sortedList.add(nums[i])
            #print index, sortedList, ans
        return ans