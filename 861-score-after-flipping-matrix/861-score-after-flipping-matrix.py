class Solution(object):
    def matrixScore(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def row(grid):
            for j in range(len(grid)):
                if(grid[j][0]==0):
                    for i in range(0,len(grid[0])):
                        grid[j][i]=1-grid[j][i]
            return grid
        def column(grid):
            for i in range(0,len(grid[0])):
                zero=0
                one=0
                for j in range(0,len(grid)):
                    if(grid[j][i]==0):
                        zero+=1
                    else:
                        one+=1
                if(zero>one):
                    for j in range(0,len(grid)):
                        grid[j][i]=1-grid[j][i]
            return grid
        grid=row(grid)
        grid=column(grid)
        ans=0
        #print(grid)
        for i in grid:
            s=""
            for j in i:
                s+=str(j)
            ans+=int(s,2)
        return ans        