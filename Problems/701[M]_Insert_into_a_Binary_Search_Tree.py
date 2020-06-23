# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
  def insertIntoBST(self, root, val):
    """
    :type root: TreeNode
    :type val: int
    :rtype: TreeNode
    """
    queue = [root]
    while queue:
      tmp = queue.pop(0)
      if tmp is None:
        return TreeNode(val)
      if val > tmp.val:
        if not tmp.right:
          tmp.right = TreeNode(val)
          break
        else:
          queue.append(tmp.right)
      elif val < tmp.val:
        if not tmp.left:
          tmp.left = TreeNode(val)
          break
        else:
          queue.append(tmp.left)
    return root

