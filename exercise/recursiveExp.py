# A recursive implementation for computing x ** n where n is an integer.
# O(log n)
def exp(x, n):
    if n == 0:
        return 1
    global count
    count += 1
    result = exp(x * x, n // 2)

    if n % 2 == 0:
        return result
    else:
        return x * result

count = 0
print(exp(2, 3), " ", count)
count = 0
print(exp(2, 4), " ", count)
count = 0
print(exp(2, 50), " ", count)
count = 0
print(exp(2, 100), " ", count)
count = 0
print(exp(2, 100), " ", count)
