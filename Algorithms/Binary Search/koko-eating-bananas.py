class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, sum(piles)
        while left < right:
            mid = left + (right - left) // 2
            if self.canEat(piles, mid, h):
                right = mid
            else:
                left = mid + 1
        return left

    def canEat(self, piles, threshold, target_hour):
        hours = 0
        for pile in piles:
            hours += math.ceil(pile / threshold)
        return hours <= target_hour
