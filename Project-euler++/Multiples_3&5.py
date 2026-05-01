def sum_of_multiples(n, k):
    m = (n - 1) // k
    return k * m * (m + 1) // 2

Test_case = int(input())
for _ in range(Test_case):
    n = int(input())
    result = sum_of_multiples(n, 3) + sum_of_multiples(n, 5) - sum_of_multiples(n, 15)
    print(result)
