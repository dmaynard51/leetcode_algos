class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort()
        
        lend = intervals[0][1]
        res = 0
        for i in range(1,(len(intervals))):
            start, end = intervals[i][0], intervals[i][1]
            if start >= lend:
                lend = end
            else:
                res += 1
                lend = min(lend, end)
        return res