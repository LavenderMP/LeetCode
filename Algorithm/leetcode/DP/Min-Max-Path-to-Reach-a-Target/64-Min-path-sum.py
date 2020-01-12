"""
https://leetcode.com/problems/minimum-path-sum/
Given a m x n grid filled with non-negative numbers,
find a path from top left to bottom right which minimizes the sum of all numbers along its path.
Note: You can only move either down or right at any point in time.

Example:
Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
"""

GRID = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]

def solution(GRID):
    for i in range(len(GRID)):
        for j in range(len(GRID[0])):
            if i == 0 and j == 0:
                continue
            elif i == 0 and j != 0:
                GRID[i][j] = GRID[i][j] + GRID[i][j-1]
            elif j == 0 and i != 0:
                GRID[i][j] = GRID[i][j] + GRID[i-1][j] 
            else:
                GRID[i][j] = min(GRID[i-1][j], GRID[i][j-1]) + GRID[i][j]
    return GRID[len(GRID)-1][len(GRID[0])-1]
print(solution(GRID))