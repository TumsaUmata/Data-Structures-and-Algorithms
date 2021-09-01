from collections import deque


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = deque()
        left, right = 0, len(nums) - 1
        while left <= right:
            left_square = nums[left] * nums[left]
            right_square = nums[right] * nums[right]
            if left_square > right_square:
                result.appendleft(left_square)
                left += 1
            else:
                result.appendleft(right_square)
                right -= 1

        return result