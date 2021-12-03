arr = []

for _ in range(9):
    arr.append(list(map(int, input().rstrip().split())))
max_value = 0
max_row = 0
for i in range(len(arr)):
    if max_value < max(arr[i]):
        max_value = max(arr[i])
        max_row = i

max_column = arr[max_row].index(max_value)

print(max_value)
print(max_row+1, max_column+1)

# print(len(arr))
