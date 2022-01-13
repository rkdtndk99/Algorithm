import sys
input = lambda : sys.stdin.readline().strip()

n = int(input())
for _ in range(n):
    str = input()
    array = str.split()
    for i in range(len(array)):
        array[i] = array[i][::-1]
    print(' '.join(array))