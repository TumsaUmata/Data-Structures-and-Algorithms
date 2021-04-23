class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        if not wall or len(wall) == 0:
            return 0

        m = len(wall)
        width = sum(wall[0])
        slots = defaultdict(int)

        for i in range(m):
            row_sum = 0
            for j in range(len(wall[i])):
                row_sum += wall[i][j]
                slots[row_sum] += 1

        max_sum = 0
        for row_sum in slots:
            if row_sum != width:
                max_sum = max(max_sum, slots[row_sum])

        return m - max_sum
