class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr) - 1
        while left + k <= right:
            if arr[right] - x >= x - arr[left]:
                right -= 1
            else:
                left += 1

        return arr[left: left + k]


class Solution2:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr) - k
        while left < right:
            mid = (left + right) // 2
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        return arr[left:left + k]

"""
Time Complexity and Space Complexity:
Solution 1: O(N) and O(1) --- two pointers
Solution 2: O(LogN) and O(1) --- binary search

Other solutions:
Naive Solution: We can sort all the array depending on their absolute value difference, then return k. 
Better Solution: We can heap -- O(NlogK) TC and O(K) SC
"""