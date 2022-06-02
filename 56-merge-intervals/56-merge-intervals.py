class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        
        intervals.sort(key = lambda i: i[0])
        
        for i in range(len(intervals)):
            if len(res) == 0:
                res.append(intervals[i])
            else:
                if res[-1][1] >= intervals[i][0]:
                    res[-1][1] = max(res[-1][1], intervals[i][1])
                else:
                    res.append(intervals[i])
        return res