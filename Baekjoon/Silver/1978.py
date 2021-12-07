n = int(input())
count = 0
numbers = list(map(int, input().rstrip().split()))
for i in range(n):
    number = numbers[i]
    if number == 2:
        count += 1
    elif number == 1:
        count += 0
    else:
        error = 0
        for j in range(2, number):
            if number % j != 0:
                error += 0
            else:
                error += 1
        if error == 0:
            count += 1
        else:
            count += 0

print(count)