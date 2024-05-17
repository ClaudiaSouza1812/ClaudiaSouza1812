
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[j]:
                j += 1
                nums[j] = nums[i]
        k = len(nums)
        return k
Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4])

from collections import OrderedDict

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = list(OrderedDict.fromkeys(nums))
        return len(k)
Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4])

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums[:] = sorted(set(nums))
        return len(nums)
Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4])

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = list(set(nums))
        nums.sort()
        return len(nums)
Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4])

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[j]:
                j += 1
                nums[j] = nums[i]

        return j + 1

Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4])
