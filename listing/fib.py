# Compute the nth number in the Fibonacci sequence.
def fib( n ):
    assert n >= 1, "Fibonacci not defined for n < 1."
    if n == 1 :
        return 1
    else :
        return fib(n - 1) + fib(n - 2)

fib(6)
