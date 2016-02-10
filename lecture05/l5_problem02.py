def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    # Your code here
    if exp == 0:
        return 1
    elif exp == 1:
        return base
    else:
        return base * recurPower(base, exp-1)

# ----------
# Test cases
# ----------

print recurPower(-9.01, 0)     # ==> 1.0000
print recurPower(6.48, 9)      # ==> 20145360.9346
print recurPower(0.56, 3)      # ==> 0.1756
print recurPower(-9.6, 3)      # ==> -884.7360
print recurPower(-8.37, 1)     # ==> -8.3700
print recurPower(6.89, 7)      # ==> 737113.8193
print recurPower(0.64, 10)     # ==> 0.0115
print recurPower(-1.07, 10)    # ==> 1.9672
