class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        start, end = [], []
        
        for s, e in intervals:
            start.append(s)
            end.append(e)
        start.sort()
        end.sort()
        
        s, e = 0, 0
        count,res = 0, 0
        while s < len(intervals):
            if start[s] < end[e]:
                count += 1
                s += 1
            else:
                count -=1
                e += 1
            res = max(count, res)
        return res