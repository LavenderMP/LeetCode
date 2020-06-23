# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

  def __str__(self):
    return str(self.val)


def inorder_traveral(root):
  # pass
  if root is None:
    return
  inorder_traveral(root.left)
  print(root.val, " ")
  inorder_traveral(root.right)


arr = [3, 2, 1, 6, 0, 5]


def Solution(nums):
  stack = []
  for num in arr:
    cur = TreeNode(num)
    while stack and stack[-1].val < cur.val:
      cur.left = stack.pop()
    if stack:
      stack[-1].right = cur
    stack.append(cur)
  return stack[0]


result = Solution(arr)
# print(result)
print(inorder_traveral(result))
