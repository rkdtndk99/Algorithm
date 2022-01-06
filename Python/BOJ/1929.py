def is_prime_sieve(n, start):
    sieve = [True] * (n+1)
    sieve[0], sieve[1] = False, False

    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i + i, n+1, i):
                sieve[j] = False

    return [i for i in range(start, n+1) if sieve[i] == True]

min, max = map(int,input().split())
for k in sorted(is_prime_sieve(max, min)):
    print(k)