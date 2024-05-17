
# solution using the sorting algorithm
# Time complexity: O(nlogn)
# Space complexity: O(1)

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return nums[len(nums) // 2]

Solution().majorityElement([1,1,1,2,2,2,2])

# equivalent to the following code using the max function
# Time complexity: O(n)
# Space complexity: O(n)

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x = max(set(nums), key = nums.count)
        return x

Solution().majorityElement([1,1,1,2,2,2,2])

# equivalent to the following code using the Counter class
# Time complexity: O(n)
# Space complexity: O(n)

from collections import Counter

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return Counter(nums).most_common(1)[0][0]

Solution().majorityElement([1,1,1,2,2,2,2])

# equivalent to the following code using the dictionary
# Time complexity: O(n)
# Space complexity: O(n)

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = {}
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1

        return max(counts, key=counts.get)

Solution().majorityElement([1,1,1,2,2,2,2])

# equivalent to the following code using the Boyer-Moore Voting Algorithm
# Time complexity: O(n)
# Space complexity: O(1)

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = 0
        n = None

        for num in nums:
            if c == 0:
                n = num
            c += (1 if num == n else -1)

        return n

Solution().majorityElement([1,1,1,2,2,2,2])

# equivalent to the following code using the divide and conquer algorithm
# Time complexity: O(nlogn)
# Space complexity: O(logn)

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.majorityElementRec(nums, 0, len(nums))

    def majorityElementRec(self, nums, lo, hi):
        if lo == hi - 1:
            return nums[lo]

        mid = (hi - lo) // 2 + lo
        left = self.majorityElementRec(nums, lo, mid)
        right = self.majorityElementRec(nums, mid, hi)

        if left == right:
            return left

        leftCount = sum(1 for i in range(lo, hi) if nums[i] == left)
        rightCount = sum(1 for i in range(lo, hi) if nums[i] == right)

        return left if leftCount > rightCount else right

Solution().majorityElement([1,1,1,2,2,2,2])


import sys

with open("user.out", 'w') as f:
    for line in sys.stdin:
        l = sorted(map(int, line.rstrip()[1:-1].split(',')))
        f.write(str(l[len(l) // 2]) + '\n')
exit(0)



def process_line(line):
    l = sorted(map(int, line.rstrip()[1:-1].split(',')))
    return str(l[len(l) // 2])

with open("input.txt", 'r') as input_file, open("user.out", 'w') as output_file:
    for line in input_file:
        output_file.write(process_line(line) + '\n')