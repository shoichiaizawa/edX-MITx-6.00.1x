def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    numS = min(a, b)
    numL = max(a, b)
    gdc = 0

    for divisor in range(1, numS+1):
        if numS % divisor == 0 and numL % divisor == 0:
            gdc = divisor

    return gdc

# ----------
# Test cases
# ----------

print gcdIter(49, 126)   # ==> 7
print gcdIter(72, 192)   # ==> 24
print gcdIter(77, 11)    # ==> 11
print gcdIter(96, 336)   # ==> 48
print gcdIter(44, 30)    # ==> 2
print gcdIter(120, 40)   # ==> 40
print gcdIter(21, 15)    # ==> 3
print gcdIter(176, 99)   # ==> 11
print gcdIter(27, 72)    # ==> 9
print gcdIter(4, 20)     # ==> 4

# -----------------------------------------------------------------------------

# NOTES: Sample answer

# def gcdIter(a, b):
#     '''
#     a, b: positive integers
#
#     returns: a positive integer, the greatest common divisor of a & b.
#     '''
#     testValue = min(a, b)
#
#     # Keep looping until testValue divides both a & b evenly
#     while a % testValue != 0 or b % testValue != 0:
#         testValue -= 1
#
#     return testValue
