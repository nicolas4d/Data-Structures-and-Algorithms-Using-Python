# A recursive implementation for computing x ** n where n is an integer.
def exp(x, n):
    if n == 0:
        return 1

    result = exp(x * x, n // 2)

    if n % 2 == 0:
        return result
    else:
        return x * result

print(exp(1, 100))
print(exp(2, 100))
