import math 

#!! Input Statements
test_cases = int(input().strip())
res = int()
mod = 10**9 + 7
for __ in range(test_cases):
    n, m = map(int, input().split())

    num = math.factorial(n + m)  
    den = math.factorial(n)* math.factorial(m)

    res = (num * (1/den)) % mod

print(int(res))