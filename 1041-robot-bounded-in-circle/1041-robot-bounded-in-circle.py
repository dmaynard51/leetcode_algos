class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        x, y = 0, 0
        dx, dy = 0, 1
        
        for i in instructions:
            if i == 'L':
                dx, dy = -dy, dx
            elif i == 'R':
                dx, dy = dy, -dx
            elif i == 'G':
                x, y = (x + dx), (y + dy)
        return (x,y) == (0, 0) or (dx, dy) != (0, 1)