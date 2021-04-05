class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr) - 1
        while left + k <= right:
            if arr[right] - x >= x - arr[left]:
                right -= 1
            else:
                left += 1

        return arr[left: left + k]
