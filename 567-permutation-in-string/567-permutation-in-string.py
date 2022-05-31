class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        dct1 = collections.Counter(s1)
        counter = 0
        l = 0
        for r in range(len(s2)):
            if s2[r] in dct1:
                dct1[s2[r]] -= 1
                if dct1[s2[r]] == 0:
                    counter += 1
                
            if r >= len(s1):
                if s2[l] in dct1:
                    if dct1[s2[l]] == 0:
                        counter -= 1
                    dct1[s2[l]] += 1
                l+=1

            if counter == len(dct1):
                return True
        return False