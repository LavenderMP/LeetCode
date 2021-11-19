# Find Minimum in Rotated Sorted Array
arr = [4,5,1,2,3]
def find_min(nums):
  left, right = 0, len(nums) - 1
  while nums[left] > nums[right]:
    middle = (left + right) // 2
    if nums[middle] < nums[right]:
      right = middle
    else:
      left = middle + 1
  return nums[left]

arr1 = [1]
print(find_min(arr1))