X = int(input())
cnt = 0
while X != 1:
    if X % 6 == 0:
        X = X/6
        cnt += 1
    elif X % 3 == 0:
        X = X/3
        cnt += 1
    elif X % 2 == 0:
        X = X / 2
        cnt += 1
    else:
        X -= 1

print(cnt)