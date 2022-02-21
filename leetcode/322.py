
# recursion with memo
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [-1] * (amount + 1)
        memo[0] = 0
        def findchange(amount):
            
            if memo[amount] != -1:
                return memo[amount]
            ans = float('inf')
            for coin in coins:
                if coin <= amount:
                    if memo[amount] != -1:
                        ans = min(ans, memo[amount])
                    else:
                        sub_ans = 1 + findchange(amount-coin)
                        ans = min(ans, sub_ans)
            memo[amount] = ans
            return ans
        change = findchange(amount)
        if change == float('inf'):
            return -1
        return change
                    
# DP
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], 1+dp[i-coin])
        if dp[amount] > amount:
            return -1
        return dp[amount]
        