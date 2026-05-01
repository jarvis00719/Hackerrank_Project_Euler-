import numpy as np

##

#!! Input Statements
test_cases = int(input().strip())

for _ in range(test_cases):

    rows, cols = map(int, input().split())

    n, m  =np.indices((rows, cols))

    coods = np.stack((n, m), axis=-1)

    print(coods)