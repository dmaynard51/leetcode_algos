class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        nums1.sort()
        nums2.sort()
        set1 = set(nums1)
        set2 = set(nums2)
        res1 = []
        res2 = []
        i = 0
        while i < len(nums1):
            while i+1 < len(nums1) and nums1[i] == nums1[i+1]:
                i+= 1
            if nums1[i] not in set2:
                res1.append(nums1[i])
            i+=1
        i =0
        while i < len(nums2):
            while i+1 < len(nums2) and nums2[i] == nums2[i+1]:
                i+= 1            
            if nums2[i] not in set1:
                res2.append(nums2[i])
            i+= 1
        
        return [res1, res2]