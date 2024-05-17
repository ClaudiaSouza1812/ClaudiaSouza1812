
class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        wealth = [0] * len(accounts)

        for i in range(len(accounts)):
            for n in accounts[i]:
                wealth[i] = wealth[i] + n

        richest = max(wealth)
        return richest

list = [[1,2,3],[3,2,1]]
s = Solution()
s.maximumWealth(list)


class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        richest = 0

        for i in range(len(accounts)):
            wealth = 0
            for n in accounts[i]:
                wealth = wealth + n
            richest = max(richest, wealth)

        return richest

list = [[1,2,3],[3,2,1]]
s = Solution()
s.maximumWealth(list)


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth = [0] * len(accounts)

        for i in range(len(accounts)):
            wealth[i] = sum(accounts[i])

        richest = max(wealth)
        return richest

list = [[1,2,3],[3,2,1]]
s = Solution()
s.maximumWealth(list)


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        richest = 0

        for i in range(len(accounts)):
            wealth = 0
            for n in accounts[i]:
                wealth = wealth + n
            richest = max(richest, wealth)

        return richest

list = [[1,2,3],[3,2,1]]
s = Solution()
s.maximumWealth(list)
