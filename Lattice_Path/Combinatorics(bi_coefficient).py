##🔹 Solution Approaches
#1. Combinatorics (Binomial Coefficient)

#Each path is a sequence of moves: 

## 𝑛 downs + 𝑚 rights.
## Total moves = 𝑛 + 𝑚.
##You just need to choose positions for downs (or rights).

## Formula:- "Binomial coeffcient"

import math 

#!! Input Statements
test_cases = int(input().strip())
 
for __ in range(test_cases):
    n, m = map(int, input().split())

    num = math.factorial(n + m)  
    den = math.factorial(n)* math.factorial(m)

    result = int(num/den)
    print(result)


