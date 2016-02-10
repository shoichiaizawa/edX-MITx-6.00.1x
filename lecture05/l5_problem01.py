def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    # Your code here
    result = 1
    while exp > 0:
        result *= base
        exp -= 1
    return result

# Test cases:
print iterPower(0.18, 0)    # ==> 1.0000
print iterPower(-9.97, 1)   # ==> -9.8700
print iterPower(2.9, 10)    # ==> 42070.7233
print iterPower(7.41, 6)    # ==> 165542.4002
print iterPower(-7.21, 1)   # ==> -7.2100
print iterPower(-8.1, 4)    # ==> 4304.6721
print iterPower(-8.58, 7)   # ==> -3423032.4399
print iterPower(-3.3, 7)    # ==> -4261.8443

# -----------------------------------------------------------------------------

# NOTES: Sample answer

# def recurPower(base, exp):
#     '''
#     base: int or float.
#     exp: int >= 0
#
#     returns: int or float, base^exp
#     '''
#     # Base case is when exp = 0
#     if exp <= 0:
#         return 1
#
#     # Otherwise, exp must be > 0, so return
#     #  base* base^(exp-1). This is the recursive case.
#     return base * recurPower(base, exp - 1)
