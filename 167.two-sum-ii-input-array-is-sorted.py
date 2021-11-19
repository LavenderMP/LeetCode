#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#
from typing import *
# @lc code=start
def find_upper(arr, target):
    """next smallest larger index in given sorted array
    """
    left = 0
    right = len(arr)-1
    while left < right:
        mid = (left + right)//2
        if arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid
        else:
            return mid+1
    return left

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Solution 1: Using hash table O(n) Time, O(n) Space
        # hashTable = {}
        # for i, n in enumerate(numbers):
        #     left_over = target - n
        #     if n in hashTable:
        #         return hashTable[n], i +1
        #     elif n > target:
        #         break
        #     else:
        #         hashTable[left_over] = i + 1
        # Solution 2: Using two pointers
        low = 0
        high = find_upper(numbers, target)
        while low < high:
            target_val =  numbers[low] + numbers[high]
            if  target_val == target:
                return [low+1, high+1]
            elif target_val > target:
                high -= 1
            else:
                low += 1
            
# @lc code=end

