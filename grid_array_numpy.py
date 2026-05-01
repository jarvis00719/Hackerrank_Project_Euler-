
import numpy as np
import math

#!! Input Statements
test_cases = int(input().strip())

multiple_inputs = list(map(int,(input().split())))

for _ in range(test_cases):
    n, m = multiple_inputs[0], multiple_inputs[1]

    paths_num = math.factorial((n+m))
    paths_den = math.factorial((n*m))

    fin_path = paths_num/paths_den

    print(fin_path)
