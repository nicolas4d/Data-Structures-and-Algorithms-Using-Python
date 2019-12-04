# Design and implement a recursive function for computing the greatest common
# divisor of two integer values.

# analysis:
# Lower integer is biger integer's divisor then greatest common divisor.
# otherwise, [lower integer - 1] an so on.

def bigestDivisor(valueOne, valueTwo):
    "Get greatest common divisor of two integer values."

    if valueOne > valueTwo:
        big = valueOne
        small = valueTwo
    elif valueOne == valueTwo:
        return valueOne
    else :
        big = valueTwo
        small = valueOne

    return bigestDivisorRec(big, small, small)

def bigestDivisorRec(big, small, div):
    if big % div == 0 and small % div == 0:
        return div
    else :
        return bigestDivisorRec(big, small, div - 1)

print(bigestDivisor(10, 5))
print(bigestDivisor(10, 3))
print(bigestDivisor(10, 10))
