def recurPowerNew(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float; base^exp
    '''
    # Your code here
    if exp == 0:
        return 1
    elif exp > 0 and exp % 2 == 1:
        return base * recurPowerNew(base, exp-1)
    elif exp > 0 and exp % 2 == 0:
        return recurPowerNew(base*base, exp/2)

# ----------
# Test cases
# ----------

print recurPowerNew(3.88, 0)    # ==> 1.0000
print recurPowerNew(-1.45, 4)   # ==> 4.4205
print recurPowerNew(3.36, 2)    # ==> 11.2896
print recurPowerNew(-2.99, 10)  # ==> 57109.9636
print recurPowerNew(4.1, 3)     # ==> 68.9210
print recurPowerNew(-5.38, 0)   # ==> 1.0000
print recurPowerNew(0.2, 7)     # ==> 0.0000
print recurPowerNew(7.62, 2)    # ==> 58.0644

# -----------------------------------------------------------------------------

# NOTES: Sample answer

# def recurPowerNew(base, exp):
#     '''
#     base: int or float.
#     exp: int >= 0
#
#     returns: int or float; base^exp
#     '''
#     # Base case is when exp = 0
#     if exp <= 0:
#         return 1
#
#     # Recursive case 1: exp > 0 and even
#     elif exp % 2 == 0:
#         return recurPowerNew(base*base, exp/2)
#
#     # Otherwise, exp must be > 0 and odd, so use the second
#     #  recursive case.
#     return base * recurPowerNew(base, exp - 1)
