def fact( n ):
    assert n >= 0, "Factorial not defined for negative values."
    if n < 2 :
        return 1
    else :
        return n * fact(n - 1)

def binomialCoefficient(n, r):
    return fact(n) // (fact(r) * fact(n - r))

# print(binomialCoefficient(0, 0))
# print(binomialCoefficient(1, 0))
# print(binomialCoefficient(1, 1))
# print(binomialCoefficient(2, 1))
# print(binomialCoefficient(2, 2))

def pascalTriangleLine(n):
    """line of pascal Triangle."""
    assert n >= 0, "number has to be bigger then 0"

    line = list()

    for i in range(n + 1):
        # print(binomialCoefficient(n, i), end=" ")
        line.append(binomialCoefficient(n, i))

    return line

def pascalTriangle(n):
    """n is how many lines."""
    assert n >= 0, "n >= 0"

    for i in range(n):
        print(pascalTriangleLine(i))

pascalTriangle(6)
pascalTriangle(10)

