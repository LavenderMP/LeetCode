"""
https://leetcode.com/problems/min-cost-climbing-stairs/
On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

Once you pay the cost, you can either climb one or two steps.
You need to find minimum cost to reach the top of the floor,
and you can either start from the step with index 0,
or the step with index 1.

Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.

Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].
"""
cost1 = [10, 15, 20]
cost2 = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
def solution(cost, dp = {}):
    dp[0] = cost[0]
    dp[1] = cost[1]
    for i in range(2, len(cost)+1):
       minval = 0 if i == len(cost) else cost[i]
       dp[i] = min(dp[i-1], dp[i-2]) + minval
    return dp[len(cost)]

print(solution(cost1))
print(solution(cost2))
# Solution if you want Compute i-th floors just compare the last two i-1 and i-2(th).