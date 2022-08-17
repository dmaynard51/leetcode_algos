class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        visit = set()
        dct = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        for word in words:
            temp = ''
            
            for c in word:
                temp += dct[ord(c) - ord('a')]
            visit.add(temp)
        
        return len(visit)