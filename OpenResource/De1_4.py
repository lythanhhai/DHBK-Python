result = lambda n : 1 if(n == 1 or n == 0) else n * result(n - 1)
print(result(5))
