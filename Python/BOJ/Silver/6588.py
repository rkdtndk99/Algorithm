import sys

r = 1000000

sieve = [True for _ in range(r)]

for i in range(2, int(r**0.6)):
    if sieve[i]:
        for j in range(i + i, r, i):
            sieve[j] = False

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    for k in range(3, r):
        if sieve[k]:
            if sieve[n-k]:
                print("%d = %d + %d"%(n , k , n-k))
                break