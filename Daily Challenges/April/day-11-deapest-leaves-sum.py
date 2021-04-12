# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        result = 0
        if not root:
            return result

        queue = deque()
        queue.append(root)
        while queue:
            level_size = len(queue)
            level_sum = 0
            for _ in range(level_size):
                current_node = queue.popleft()
                level_sum += current_node.val

                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
            result = level_sum

        return result
