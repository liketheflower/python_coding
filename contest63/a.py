class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        dp = [0 for _ in range(len(cost))]
        dp[0] = cost[0]
        dp[1] = cost[1]
        
        for i in range(2, len(dp)):
            dp[i] = min(dp[i - 2], dp[i - 1]) + cost[i]
        
        return min(dp[-1], dp[-2])

a=Solution()
b  = [10, 15, 20]
b = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
print a.minCostClimbingStairs(b)

         
