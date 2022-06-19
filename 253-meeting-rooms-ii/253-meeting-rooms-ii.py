class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        
        start = sorted(i[0] for i in intervals)
        end = sorted(i[1] for i in intervals)
        
        s, e = 0, 0
        res = 0
        count = 0
        while s < len(intervals):
            if start[s] < end[e]:
                count += 1
                s += 1
            else:
                e += 1
                count -=1
            res = max(res, count)
        return res