class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0

        n, m = len(matrix), len(matrix[0])
        dp = defaultdict(int)
        max_path = 0
        for r in range(n):
            for c in range(m):
                max_path = max(max_path, self.traverse(matrix, r, c, dp))

        return max_path

    def traverse(self, matrix, row, col, dp):
        if (row, col) in dp:
            return dp[(row, col)]

        temp = 1
        longest = 1
        if row > 0 and matrix[row - 1][col] > matrix[row][col]:
            temp = max(temp, self.traverse(matrix, row - 1, col, dp) + 1)
        if row < len(matrix) - 1 and matrix[row + 1][col] > matrix[row][col]:
            temp = max(temp, self.traverse(matrix, row + 1, col, dp) + 1)
        if col > 0 and matrix[row][col - 1] > matrix[row][col]:
            temp = max(temp, self.traverse(matrix, row, col - 1, dp) + 1)
        if col < len(matrix[0]) - 1 and matrix[row][col + 1] > matrix[row][col]:
            temp = max(temp, self.traverse(matrix, row, col + 1, dp) + 1)

        dp[(row, col)] = temp
        longest = max(longest, temp)
        return longest
