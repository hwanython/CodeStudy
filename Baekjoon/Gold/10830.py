n, b = map(int, input().split())
A = []
for _ in range(n):
  A.append(list(map(int, input().split())))

def power(M, n):
  if n == 1:
      for i in range(len(M)):
          for j in range(len(M)):
              M[i][j] %= 1000
      return M
  a = power(M, n // 2)
  res = mat_multi(a,a)
  if n % 2 == 0:
    return res
  else:
    return mat_multi(M, res)

def mat_multi(A, B):
  C = [[0] * n for _ in range(n)]
  for i in range(n):
    for j in range(n):
      for l in range(n):
          C[i][j] += A[i][l] * B[l][j]
      C[i][j] %= 1000
  return C

result = power(A, b)

for x in result:
  for y in x:
    print(y, end = ' ')
  print()