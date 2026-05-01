## Calculation (Binomial Coefficient)

import math

n = 3
m = 2

num = math.factorial(n + m)  
den = math.factorial(n)* math.factorial(m)

result = int(num/den)


print(result)