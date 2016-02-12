def integerDivision(x, a):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the integer division of x divided by a.
    """
    count = 0
    while x >= a:
        count += 1
        x = x - a
    return count

# ----------
# Test cases
# ----------

print integerDivision(5, 3)    # ==> 1

# -------------------------------
# More test cases from the grader
# -------------------------------

print integerDivision(5, 3)    # ==> 1
print integerDivision(34, 3)   # ==> 11
print integerDivision(26, 2)   # ==> 13
print integerDivision(40, 8)   # ==> 5
print integerDivision(31, 10)  # ==> 3
