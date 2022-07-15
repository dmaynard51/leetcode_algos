class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        #for word in array.split()[1:]:
        numbers = []
        letters = []
        nums = "123456789"
        
        for log in logs:
            if log.split()[1].isdigit():
                numbers.append(log)
            else:
                letters.append(log)

        letters.sort(key = lambda x: x.split()[0])            #when suffix is tie, sort by identifier
        letters.sort(key = lambda x: x.split()[1:])
        #letters.sort(key = lambda x: x.split()[1:])             #sort by suffix
        #print letters
        result = letters + numbers
        return result