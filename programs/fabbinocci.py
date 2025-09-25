class Solution:
    def series(self, n):

        MOD = 10 ** 9 + 7
        if n == 0:
            return [0]
        if n <= 1:
            return [0, 1]

        fib = [0, 1]
        for i in range(2, n + 1):
            fib.append((fib[-1] + fib[-2]) % MOD)

        return fib
sol=Solution()
print(sol.series(10))