
## Good for larger grids !!

MOD = 10**9 + 7

# Precompute factorials up to max possible n+m
MAX = 2 * 10**6   # adjust based on constraints
fact = [1] * (MAX+1)
for i in range(1, MAX+1):
    fact[i] = fact[i-1] * i % MOD

# Fast modular exponentiation
def mod_pow(a, b, mod):
    res = 1
    while b > 0:
        if b % 2:
            res = res * a % mod
        a = a * a % mod
        b //= 2
    return res

# Modular inverse using Fermat's theorem
def mod_inv(a, mod):
    return mod_pow(a, mod-2, mod)

test_cases = int(input().strip())
for _ in range(test_cases):
    n, m = map(int, input().split())
    res = fact[n+m] * mod_inv(fact[n], MOD) % MOD
    res = res * mod_inv(fact[m], MOD) % MOD
    print(res)
