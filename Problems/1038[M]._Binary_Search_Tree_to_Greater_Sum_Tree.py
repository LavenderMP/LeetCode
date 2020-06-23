# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        inorder_traversal(root)
        return root
def inorder_traversal(node, tmp = 0):
    if not node:
        return 0
    curNode = node.val
    right_sum = inorder_traversal(node.right, tmp)
    swap = right_sum + curNode + tmp
    node.val = swap
    left_sum = inorder_traversal(node.left, swap)
    return right_sum + left_sum + curNode
    
