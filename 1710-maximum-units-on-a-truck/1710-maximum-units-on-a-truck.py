class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        boxTypes.sort(key = lambda i: (i[1]), reverse = True)
        
        res = 0
        
        for numBoxes, unitsPer in boxTypes:
            if truckSize >= numBoxes:
                res += (numBoxes * unitsPer)
                truckSize -= numBoxes
            elif truckSize < numBoxes:
                res += (truckSize * unitsPer)
                truckSize -= truckSize
        return res