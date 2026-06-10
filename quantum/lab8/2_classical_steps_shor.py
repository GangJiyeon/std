from math import gcd
# shor's alghrithm
def shor_classical(a, N):
    # if a and N are not coprime, return gcd(a, N)
    if gcd(a, N) > 1:
        return gcd(a, N)
    
    # find the period r of a mod N
    r, x = 1, a % N
    while x != 1:
        x = (x * a) % N
        r += 1
    
    # if r is odd, return None
    if r % 2:
        return None

    # calculate h = a ^(r/2) mod N
    h = pow(a, r // 2, N)

    # calculate p = gcd(h + 1, N), q = qcd(h = 1, N)
    p = gcd(h + 1, N)
    q = gcd(h - 1, N)
    if 1 < p < N: return p
    if 1 < q < N: return q
    return None

# test the shor's algorithm
for N in [15, 21, 33, 35]:
    # find the values of a that work
    wins = [a for a in range(2, N) if shor_classical(a, N)]
    # print the number of values of a that work
    print(f"N={N}: {len(wins)}/{N-2} a-values work")