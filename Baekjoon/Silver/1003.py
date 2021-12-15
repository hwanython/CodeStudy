import sys


def fibo(nowNo, st):
    if nowNo == st:
        print(memo[st][0], memo[st][1])
    else:
        memo.append([memo[-1][0] + memo[-2][0], memo[-1][1] + memo[-2][1]])
        fibo(nowNo + 1, st)


caseNo = int(sys.stdin.readline())

for i in range(caseNo):
    memo = [[1, 0], [0, 1], [1, 1]]
    Nth_fibo = int(sys.stdin.readline())
    if Nth_fibo == 0:
        print(1, 0)
    elif Nth_fibo == 1:
        print(0, 1)
    else:
        fibo(2, Nth_fibo)

