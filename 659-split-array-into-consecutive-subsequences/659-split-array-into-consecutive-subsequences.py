class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        counter = collections.Counter(nums)
        seq = defaultdict(int)
        
        for num in nums:
            if counter[num] == 0:
                continue
            elif seq[num] > 0:
                seq[num] -= 1
                seq[num+1] += 1
            elif counter[num + 1] > 0 and counter[num + 2] > 0:
                counter[num + 1] -= 1
                counter[num + 2] -=1
                seq[num + 3] += 1
            else:
                return False
            counter[num] -= 1
        return True
        