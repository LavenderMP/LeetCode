from typing import *
alist = [1,2,3,4]
def productExceptSelf(nums: List[int]) -> List[int]:
  L = len(nums)
  
  leftside = [1] * L
  rightside = [1] * L
  
  val = 1
  for i in range(L):
      leftside[i] = val
      val *= nums[i]
  val = 1
  for i in range(L-1, -1, -1):
      rightside[i] = val
      val *= nums[i]
  print(leftside)
  print(rightside)
  output = []
  for i in range(L):
      output.append(leftside[i] * rightside[i])
  return output

productExceptSelf(alist)
