class Solution(object):
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        A = [0] + arr
        stack = [0]
        res = [0 for i in range(len(A))]

        for i in range(len(A)):
            while A[stack[-1]] > A[i]:
                stack.pop()
            j = stack[-1]
            res[i] = res[j] + (i-j) * A[i]
            stack.append(i)
        return sum(res) % (10**9 + 7)