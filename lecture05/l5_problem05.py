def gcdRecur(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if b == 0:
        return a
    else:
        return gcdRecur(b, a % b)

# ----------
# Test cases
# ----------

print gcdRecur(266, 323)  # ==> 19
print gcdRecur(42, 14)    # ==> 14
print gcdRecur(70, 84)    # ==> 14
print gcdRecur(30, 18)    # ==> 6
print gcdRecur(224, 400)  # ==> 16
print gcdRecur(26, 38)    # ==> 2
print gcdRecur(120, 375)  # ==> 15
print gcdRecur(112, 112)  # ==> 112
print gcdRecur(198, 162)  # ==> 18
print gcdRecur(196, 98)   # ==> 98

# -----------------------------------------------------------------------------

# NOTES: Euclidean algorithm
#
# Euclidean algorithm: Worked example:
# https://en.wikipedia.org/wiki/Euclidean_algorithm#Worked_example
