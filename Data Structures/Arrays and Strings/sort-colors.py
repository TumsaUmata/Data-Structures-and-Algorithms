class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = 0, len(nums) - 1
        index = 0
        while index <= right:
            if nums[index] == 0:
                nums[index], nums[left] = nums[left], nums[index]
                index += 1
                left += 1
            elif nums[index] == 1:
                index += 1
            else:
                nums[index], nums[right] = nums[right], nums[index]
                right -= 1
