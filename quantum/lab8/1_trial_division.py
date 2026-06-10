import time

# trial division algorithm
def trial(N):
    factors, p = [], 2

    # find the factors of N
    while p * p <= N:
        while N % p == 0:
            factors.append(p); N //= p
        p += 1
    if N > 1: factors.append(N)
    return factors

# test the trial division algorithm
for N in [21, 91, 1517, 1_000_003]:
    t0 = time. perf_counter()
    f = trial(N)
    dt = (time.perf_counter() - t0) * 1e6
    print(f"{N}: {f} ({dt:.1f} us)")