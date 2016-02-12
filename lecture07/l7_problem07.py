def rem(x, a):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the remainder when x is divided by a.
    """
    if x == a:
        return 0
    elif x < a:
        return x
    else:
        # rem(x-a, a)   # this does not return anything!
        return rem(x-a, a)

# ----------
# Test cases
# ----------

print rem(2, 5)  # ==> 2
print rem(5, 5)  # ==> 0
print rem(7, 5)  # ==> 2
