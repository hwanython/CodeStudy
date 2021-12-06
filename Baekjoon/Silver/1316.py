n = int(input())
input_groups = []
for _ in range(n):
    input_groups.append(input())

def find_successive(input: str):
    error = 0
    for i in range(len(input)-1):
        # error = 0
        if input[i] != input[i+1]:
            new = input[i+1:]
            if new.count(input[i]) > 0:
                error += 1
    if error == 0:
        return 1
    else:
        return 0

result = 0
for i in input_groups:
    result += find_successive(i)

print(result)
