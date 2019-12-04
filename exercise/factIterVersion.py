# Compute n!
# O(n)
def fact( n ):
    assert n >= 0, "Factorial not defined for negative values."
    if n < 2 :
        return 1
    else :
        return n * fact(n - 1)

print(fact(2))
print(fact(3))

def factIter(n):
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result

print(factIter(2))
print(factIter(3))
