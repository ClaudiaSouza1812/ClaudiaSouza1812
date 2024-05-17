
class Solution:
    def numberOfSteps(self, num: int) -> int:

        steps = 0

        while num != 0:
            if num % 2 == 0:
                num = num / 2
                steps += 1
            else:
                num = num - 1
                steps += 1
        return steps

n = 14
s = Solution()
s.numberOfSteps(n)

# equivalent to the following code using the ternary operator
class Solution:
    def numberOfSteps(self, num: int) -> int:

        steps = 0

        while num != 0:
            num = num / 2 if num % 2 == 0 else num - 1
            steps += 1
        return steps
Solution().numberOfSteps(14)
