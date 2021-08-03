class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        subsets = []
        subsets.append([])
        startIndex, endIndex = 0, 0
        for i in range(len(nums)):
            startIndex = 0
            if i > 0 and nums[i] == nums[i - 1]:
                startIndex = endIndex + 1
            endIndex = len(subsets) - 1
            for j in range(startIndex, endIndex + 1):
                subset = list(subsets[j])
                subset.append(nums[i])
                subsets.append(subset)

        return subsets