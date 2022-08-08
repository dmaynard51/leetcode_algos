class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def dfs(s, k, path, res):
            if not s and k == 4:
                res.append(path[:-1])
                return
            if k > 4:
                return
            for i in range(0,len(s)):
                
                if s[:i+1] == '0' or (s[0] != '0' and 0 < int(s[:i+1])<= 255):
                    dfs(s[i+1:], k+1, path + s[:i+1] + '.', res)
        res = []
        dfs(s, 0, "", res)
        return res