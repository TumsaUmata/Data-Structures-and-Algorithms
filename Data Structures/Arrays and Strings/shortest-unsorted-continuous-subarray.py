class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, n - 1

        while left < n - 1 and nums[left] <= nums[left + 1]:
            left += 1

        if left == n - 1:
            return 0

        while right > 0 and nums[right] >= nums[right - 1]:
            right -= 1

        subarray_min = float('inf')
        subarray_max = float('-inf')
        for i in range(left, right + 1):
            subarray_min = min(subarray_min, nums[i])
            subarray_max = max(subarray_max, nums[i])

        while left > 0 and nums[left - 1] > subarray_min:
            left -= 1

        while right < n - 1 and nums[right + 1] < subarray_max:
            right += 1

        return right - left + 1
