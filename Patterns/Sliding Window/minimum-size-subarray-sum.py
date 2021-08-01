class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLength = float('inf')
        windowStart = 0
        windowSum = 0
        for windowEnd in range(len(nums)):
            windowSum += nums[windowEnd]

            while windowSum >= target:
                minLength = min(minLength, windowEnd - windowStart + 1)
                windowSum -= nums[windowStart]
                windowStart += 1

        if minLength == float('inf'):
            return 0
        return minLength
