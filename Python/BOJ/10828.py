import sys

stack = []
n = int(input())

for _ in range(n):
    s = sys.stdin.readline().strip()
    if s.startswith("push"):
        str_list = s.split()
        num = str_list[1]
        stack.append(num)
    elif s == "top":
        if len(stack) == 0:
            print(-1)
        else :
            print(stack[len(stack)-1])
    elif s == "pop":
        if len(stack) == 0:
            print(-1)
        else :
            print(stack.pop())
    elif s == "size":
        print(len(stack))
    elif s == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)