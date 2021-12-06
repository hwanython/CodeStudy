def d(n):
    str_n = str(n)
    result = n
    for i in range(len(str_n)):
        result += int(str_n[i])
    return result

result = set(range(1,10001))
initial = set()

for i in result:
    initial.add(d(i))

non_initial = sorted(result-initial)
for i in non_initial:
    print(i)