class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        left, right = max(nums), sum(nums)
        while left < right:
            mid = left + (right - left) // 2
            if self.canSplit(nums, mid, m):
                right = mid
            else:
                left = mid + 1
        return left

    def canSplit(self, nums, threshold, target):
        count = 1
        total = 0
        for num in nums:
            total += num
            if total > threshold:
                total = num
                count += 1
                if count > target:
                    return False
        return True
