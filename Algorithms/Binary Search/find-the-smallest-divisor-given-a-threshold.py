class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left, right = 1, max(nums)
        while left < right:
            mid = left + (right - left) // 2
            s = 0
            for num in nums:
                s += ceil(num * 1.0 / mid)
            if s > threshold:
                left = mid + 1
            else:
                right = mid

        return left
