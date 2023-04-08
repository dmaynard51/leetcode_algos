class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(numbers) < 2:
            return []
        first, last = 0, len(numbers)-1
        
        while first < last:
            if numbers[first] + numbers[last] < target:
                first += 1
            elif numbers[first] + numbers[last] > target:
                last -= 1
            else:
                return [first + 1, last +1]
            