class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        two_sum_dict = {}
        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in two_sum_dict:
                return i, two_sum_dict[compliment]
            two_sum_dict[nums[i]] = i
