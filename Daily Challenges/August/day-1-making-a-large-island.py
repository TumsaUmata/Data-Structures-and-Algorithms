class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        visited = set()
        dictionary = {}

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i, j) not in visited:
                    adj_sea, area = self.bfs(grid, i, j, visited)

                    for x, y in adj_sea:
                        if (x, y) not in dictionary:
                            dictionary[(x, y)] = 0
                        dictionary[(x, y)] += area

        if len(visited) == len(grid) * len(grid[0]):
            return len(grid) * len(grid[0])

        ans = 0
        for key in dictionary:
            ans = max(ans, dictionary[key])
        return ans + 1

    def bfs(self, grid, i, j, visited):
        area = 0
        adjacent_sea = set()
        queue = collections.deque([(i, j)])
        visited.add((i, j))

        while queue:
            cx, cy = queue.popleft()
            area += 1

            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = cx + dx, cy + dy
                if not (0 <= nx < len(grid) and 0 <= ny < len(grid[0])):
                    continue
                if grid[nx][ny] == 0:
                    adjacent_sea.add((nx, ny))

                if grid[nx][ny] == 1 and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny))

        return adjacent_sea, area

