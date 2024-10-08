
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # create a list with n elements
        answer = ["1"] * n

        for i in range(2, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                answer[i - 1] = "FizzBuzz"
            elif i % 3 == 0:
                answer[i - 1] = "Fizz"
            elif i % 5 == 0:
                answer[i - 1] = "Buzz"
            else:
                answer[i - 1] = str(i)

        return answer
n = 3
s = Solution()
s.fizzBuzz(n)



