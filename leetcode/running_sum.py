

class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        new_list = []
        new_list.append(nums[0])

        for i in range(1, len(nums)):
            new_list.append(new_list[i - 1] + nums[i])
        return new_list

list = [1,2,3,4]
s = Solution()
s.runningSum(list)
