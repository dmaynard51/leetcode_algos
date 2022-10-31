class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                original = matrix[i][j]
                jj = j
                ii = i
            
                while ii < len(matrix) and jj < len(matrix[0]):
                    #print matrix[ii][jj], original
                    if matrix[ii][jj] != original:
                        return False
                    ii+= 1
                    jj+= 1

        return True
