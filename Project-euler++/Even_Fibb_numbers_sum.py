def even_fib_sum(limit):
    # First two even Fibonacci numbers
    a, b = 2, 8
    total = 0
    
    while a <= limit:
        total += a
        a, b = b, 4*b + a  # recurrence relation
    
    return total

# HackerRank style input/output
t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    print(even_fib_sum(n))
