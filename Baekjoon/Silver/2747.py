# bottom-up
N = int(input())
DP = [0 for _ in range(N+1)]
DP[1] = 1

for i in range(2, N+1): DP[i] = DP[i-1] + DP[i-2]

print(DP[N])

# Top-Down
N = int(input())
DP = [0 for _ in range(N+1)]

def fib(n):
    if n < 2: return n
    if DP[n] != 0: return DP[n]
    DP[n] = fib(n-1) + fib(n-2)
    return DP[n]


print(fib(N))