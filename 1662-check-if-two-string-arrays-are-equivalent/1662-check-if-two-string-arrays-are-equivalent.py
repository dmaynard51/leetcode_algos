class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        words1 = "".join(word1)
        words2 = "".join(word2)

        return words1 == words2