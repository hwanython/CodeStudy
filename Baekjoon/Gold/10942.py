import sys
input = sys.stdin.readline

n = int(input())
p = list(map(int,input().split()))
dp = [[0 for i in range(n)] for i in range(n)]
r = []

for i in range(int(input())):
    start, end = map(int,input().split())
    start -= 1; end -=1 #list indexing

    if start == end:
        r.append(1)
        dp[start][end] = 1
        continue

    if end - start == 1 and p[start] == p[end]:
        r.append(1)
        dp[start][end] = 1
        continue

    i, j = start, end
    while i<j:
        if p[i] == p[j]:
            if dp[i][j] ==1:
                r.append(1)
                dp[start][end]=1
                break
            i+=1; j-=1

        else:
            r.append(0)
            break
    else:
        dp[start][end] = 1
        r.append(1)
for i in r:
    print(i)
