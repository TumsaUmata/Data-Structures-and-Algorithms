class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        n, m = len(matrix), len(matrix[0])
        for i in range(n):
            for j in range(1, m):
                matrix[i][j] = matrix[i][j] + matrix[i][j - 1]

        counter = 0
        for i in range(m):
            for j in range(i, m):
                prefix_sum = {0: 1}
                current_sum = 0

                for k in range(n):
                    if i > 0:
                        current_sum += matrix[k][j] - matrix[k][i - 1]
                    else:
                        current_sum += matrix[k][j]
                    counter += prefix_sum.get(current_sum - target, 0)
                    prefix_sum[current_sum] = prefix_sum.get(current_sum, 0) + 1

        return counter
