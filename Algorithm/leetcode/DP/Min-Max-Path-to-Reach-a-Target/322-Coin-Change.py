coins = [1,2,5]

def solution(coins, amount, dp = {}):
    try:
        dp[0] = 1
        for i in range(1,amount+1):
            for coin in coins:
                if i in coins:
                    dp[i] = 1
                elif i >= coin:
                    dp[i] = min(dp[i-1], dp[i-coin]) +1
        return dp[amount]
    except KeyError:
        return -1
print(solution([1],0))