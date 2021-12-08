import sys
n = int(input())
stack_list = []
cmds = ['push', 'pop', 'size', 'empty', 'top']
for _ in range(n):
    # cmd = input().split()
    # sys.stdin.readline()이 빠르다.입력받을때,
    cmd = sys.stdin.readline().split()
    if cmd[0] == 'push':
        stack_list.append(cmd[1])
    if cmd[0] == 'pop':
        if len(stack_list) < 1:
            print(-1)
        else:
            print(stack_list[-1])
            stack_list.pop(-1)

    if cmd[0] == 'size':
        print(len(stack_list))
    if cmd[0] == 'empty':
        if len(stack_list) < 1:
            print(1)
        else:
            print(0)
    if cmd[0] == 'top':
        if len(stack_list) < 1:
            print(-1)
        else:
            print(stack_list[-1])

