class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        boxTypes.sort(key = lambda i: i[1], reverse = True)
        
        
        res = 0
        
        for boxNum, units in boxTypes:
            if truckSize >= boxNum:
                res += boxNum * units
                truckSize -= boxNum
            else:
                res += (truckSize) * units
                truckSize -= truckSize
                break
        return res
        