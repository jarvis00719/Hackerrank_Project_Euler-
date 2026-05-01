## What is the smallest positive number that is evenly divisible(divisible with no remainder) by all of the numbers from 1 to N ?
##                                                                                                                       N = int(input)!!
import math

t = int(input().strip())

for _ in range(t):
    n = int(input().strip())

    
    lcm_val = 1
    
    for i in range(1,n+1):
        lcm_val = math.lcm(lcm_val, i)
    print(lcm_val)


        
    
