# 189. Rotate Array
# Difficulty: Medium
# Time: 10/14/2020
# Given an array, rotate the array to the right by k steps, where k is non-negative.

# Follow up:
# Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
# Could you do it in-place with O(1) extra space?

# My solution submitted to LeetCode:
# Time complexity: O(n). This is because the code performs a single operation (slicing and concatenating) on each element in the list once.
# Space complexity: O(1). which means it uses a constant amount of extra space. Although the line nums[:] = nums[n - k:] + nums[:n - k]
# creates new slices, these slices are not full copies of the original list. They are smaller lists that together contain all
# the elements of the original list. The space used by these slices does not scale with the size of the input list,
# so the space complexity is constant.
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # get the length of the array
        n = len(nums)
        # the modulo operator returns the remainder of the division of the number to the left by the number to the right
        # this is to handle the case where k is greater than n, so we can get the effective k
        if k > n:
            k = k % n
        # reverse the whole array
        nums[:] = nums[n - k:] + nums[:n - k]

Solution().rotate([1,2,3,4,5,6,7], 3)

from math import ceil
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = ceil((len(nums)) / 2)
        v = nums[n:]
        del nums[n:]
        nums[:] = v + nums

        return nums

Solution().rotate([1,2,3,4,5,6,7], 3)

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = 0
        while n < k:
            v = nums.pop()
            nums.insert(0, v)
            n += 1
        return nums

Solution().rotate([1,2,3,4,5,6,7], 3)


# Solution 1: Using a new array
# Time complexity: O(n)
# Space complexity: O(n)

class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n
        new_nums = [0] * n

        for i in range(n):
            new_nums[(i + k) % n] = nums[i]

        nums[:] = new_nums
        return nums

Solution().rotate([1,2,3,4,5,6,7], 3)

# Solution 2: Using reverse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # the modulo operator returns the remainder of the division of the number to the left by the number to the right
        # this is to handle the case where k is greater than n, so we can get the effective k
        k = k % n
        # reverse the whole array
        # the [:] means the whole array
        # the -k: means the last k elements, the :-k means the first n-k elements
        # the + is to concatenate the two parts
        nums[:] = nums[-k:] + nums[:-k]
        return nums

Solution().rotate([1,2,3,4,5,6,7], 3)

# Solution 3: Using cyclic replacements
# Time complexity: O(n)
# Space complexity: O(1)

class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n
        count = 0
        start = 0
        while count < n:
            current = start
            prev = nums[start]
            while True:
                next = (current + k) % n
                nums[next], prev = prev, nums[next]
                current = next
                count += 1
                if start == current:
                    break
            start += 1
        return nums

Solution().rotate([1,2,3,4,5,6,7], 3)

# Solution 4: Using slicing
# Time complexity: O(n)
# Space complexity: O(n)

class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n
        nums[:] = nums[n-k:] + nums[:n-k]
        return nums

Solution().rotate([1,2,3,4,5,6,7], 3)


