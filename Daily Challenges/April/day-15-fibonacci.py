class Solution:
    def fib(self, n: int) -> int:
        memo = [-1 for _ in range(n + 1)]
        return self.calculateFib(n, memo)

    def calculateFib(self, n, memo):
        if n < 2:
            return n

        if memo[n] != -1:
            return memo[n]

        memo[n] = self.calculateFib(n - 1, memo) + self.calculateFib(n - 2, memo)
        return memo[n]
