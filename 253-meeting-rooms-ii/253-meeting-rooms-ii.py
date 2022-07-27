class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        start = []
        end = []
        
        for s, e in intervals:
            start.append(s)
            end.append(e)
        
        start.sort()
        end.sort()
        
        s, e = 0, 0
        
        #0,5,15
        #10,20,30
        res = 0
        count = 0
        while s < len(end):
            if start[s] < end[e]:
                s+= 1
                count += 1
            else:
                e+= 1
                count -= 1
            res = max(res, count)
        return res