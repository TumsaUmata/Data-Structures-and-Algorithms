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


class Solution3:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root:
            stack = [(root, 0)]
            while stack:
                curr_node, path_sum = stack.pop()
                path_sum += curr_node.val

                if not curr_node.left and not curr_node.right:
                    if path_sum == sum:
                        return True
                else:
                    if curr_node.left:
                        stack.append((curr_node.left, path_sum))
                    if curr_node.right:
                        stack.append((curr_node.right, path_sum))

        return False