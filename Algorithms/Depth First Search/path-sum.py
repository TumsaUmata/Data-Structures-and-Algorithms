# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False

        return self.dfs(root, targetSum)

    def dfs(self, node, targetSum):
        if not node:
            return False

        if not node.left and not node.right and node.val == targetSum:
            return True

        return self.dfs(node.left, targetSum - node.val) or self.dfs(node.right, targetSum - node.val)


class Solution2:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right and root.val == targetSum:
            return True
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)
