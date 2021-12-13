# 타뷸레이션 (상향식)

def fib(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1

    # 작은 값(소문제)부터 직접 계산하며 진행
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


fib(10)