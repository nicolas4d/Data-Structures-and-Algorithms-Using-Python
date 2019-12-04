# compute n!
def fact(n):
    assert n >= 0, "Factorial not defined for negative values."
    if n < 1:
        return 1
    else:
        return n * fact(n - 1)

print(fact(1))
print(fact(2))
print(fact(10))
