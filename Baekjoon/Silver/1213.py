S = input()

S_cnt = [0 for _ in range(26)]
for name in S:
    S_cnt[ord(name)-65] +=1

odd = 0
odd_s = ''
s = ''

for i in range(26):
    if S_cnt[i] % 2 == 1:
        odd += 1
        odd_s += chr(i+65)
    s += chr(i+65) * (S_cnt[i]//2)

if odd>1:
    print("I'm Sorry Hansoo")
else:
    print(s+odd_s+s[::-1])
