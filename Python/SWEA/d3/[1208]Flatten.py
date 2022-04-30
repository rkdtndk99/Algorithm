import sys
input = lambda : sys.stdin.readline().strip()

for k in range(10):
    dump = int(input())
    box = list(map(int, input().split()))

    for _ in range(dump):
        high = box.index(max(box))
        low = box.index(min(box))
        box[high] -= 1
        box[low] += 1

    print('#'+str(k+1), str(max(box) - min(box)))
