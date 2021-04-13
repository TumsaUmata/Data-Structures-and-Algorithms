# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        result_path = []
        self.pathSumRecursive(root, targetSum, [], result_path)
        return result_path

    def pathSumRecursive(self, node, target_sum, current_path, result_path):
        if not node:
            return

        current_path.append(node.val)
        if not node.left and not node.right and node.val == target_sum:
            result_path.append(list(current_path))
        else:
            self.pathSumRecursive(node.left, target_sum - node.val, current_path, result_path)
            self.pathSumRecursive(node.right, target_sum - node.val, current_path, result_path)

        del current_path[-1]
