class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        rows = len(matrix)
        columns = len(matrix[0])
        l = 0
        r = (rows * columns)-1
        
        
        
        while l <= r:
            m = l + (r-l)//2
            if matrix[m//columns][m%columns] > target:
                r = m -1
            else:
                l = m+ 1
        return matrix[r//columns][r%columns] == target