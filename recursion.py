def factorials(n):
    #base case to end recursion
    if n < 2:
        return 1 
    return n * factorials(n - 1)
print(factorials(4))