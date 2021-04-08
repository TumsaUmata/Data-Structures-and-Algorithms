class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        left, right = max(weights), sum(weights)
        while left < right:
            mid = left + (right - left) // 2
            if self.canShip(weights, mid, D):
                right = mid
            else:
                left = mid + 1
        return left

    def canShip(self, weights, capacity, target_day):
        days = 1
        total = 0
        for weight in weights:
            total += weight
            if total > capacity:
                total = weight
                days += 1
                if days > target_day:
                    return False

        return True
