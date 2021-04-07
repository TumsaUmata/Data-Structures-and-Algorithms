class Solution:
    def minOperations(self, n: int) -> int:
        arr = [0] * n
        for i in range(n):
            arr[i] = (2 * i) + 1

        operations = 0
        mid = n // 2
        if n % 2 == 0:
            left = mid - 1
            right = mid
        else:
            left = mid
            right = mid

        while left >= 0 and left <= right:
            operations += ((arr[right] - arr[left]) // 2)
            left -= 1
            right += 1

        return operations
