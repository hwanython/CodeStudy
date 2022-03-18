# . , ?, alphabet
# at least use "?"
#length of files is same

#입력받기
N = int(input())
A = []

for _ in range(N):
    A.append(input())
file_length = len(A[0])

cmd = ''
#값 출력
for i in range(file_length):
    char = A[0][i]
    count = 0
    for idx in range(1,N):
        if char in A[idx][i]:
            count += 1
        else:
            count += 0
    if count == N-1:
        cmd += char
    else:
        cmd += '?'
print(cmd)
