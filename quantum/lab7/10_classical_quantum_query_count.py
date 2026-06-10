def classical_bv(b: str) -> str:
    n = len(b); recovered = []
    for i in range(n):
        x = ['0'] * n; x[i] = '1'
        # Each call = 1 oracle query
        bit = sum(int(a)*int(c) for a, c in zip(x, b)) % 2
        recovered.append(str(bit))
    return ''.join(recovered[::-1])
secret = '1011010110'
found = classical_bv(secret)
print(f'classical: {found} in {len(secret)} queries')
print(f'quantum : single shot')