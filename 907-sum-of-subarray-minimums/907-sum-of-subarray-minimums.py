class Solution(object):
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
        A = [0] + arr
        
        dp = [0 for i in range(len(A))]
        
        stack = [0]
        
        for i in range(len(A)):
            while A[stack[-1]] > A[i]:
                stack.pop()
            j = stack[-1]
            dp[i] = dp[j] + (i-j)*A[i]
            stack.append(i)
        #print dp
        return sum(dp) % (10**9+7)
                
                