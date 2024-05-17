
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c, i = 0, 1
        while i < len(nums):
            if nums[i - 1] == nums[i]:
                c += 1
                if c > 1:
                    try:
                        while nums[i - 1] == nums[i]:
                            del nums[i]
                    except:
                        pass
                    c = 0
                i += 1
            else:
                c = 0
                i += 1
        return i
Solution().removeDuplicates([1,1,1])



