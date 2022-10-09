result = lambda m, n : m if n == 0 else result(n, m % n)
print(result(4, 6))
