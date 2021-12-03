strings_count = int(input().strip())

strings = []

for _ in range(strings_count):
    strings_item = input()
    strings.append(strings_item)

strings = set(strings)
strings = list(strings)
strings= sorted(strings)
strings.sort(key=len)

for i in range(len(strings)):
    print(strings[i])
