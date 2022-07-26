class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        letters = []
        digits = []
        
        for i in logs:
            if i.split()[1].isdigit():
                digits.append(i)
            else:
                letters.append(i)
        #print digits, letters
        letters.sort(key = lambda i: (i.split()[1:], i.split()[0] ))
        letters.sort(key = lambda i: (i.split()[1:]))
        return letters + digits
        #letters.sort(key = lambda i: (i.split()[1:], i.split()[0] ))