# Given apply-to-each function
def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])


# Example
def mulfive(num):
    """Multiply the input num by 5

    Args:
        num: number (integer or float)

    Returns:
        Number: a number multiplied the input num by 5

    Raises:
        TypeError: if num is not a number

    """
    return num * 5


# Problem 7a
def absList(num):
    """Get the absolute value of the input num

    Args:
        num: number (integer or float)

    Returns:
        Number: the absolute value of the input num

    Raises:
        TypeError: if num is not a number

    """
    return abs(num)


# Problem 7b
def addone(num):
    """Add 1 to the input num

    Args:
        num: number (integer or float)

    Returns:
        Number: the input num plus 1

    Raises:
        TypeError: if num is not a number

    """
    return num + 1


# Problem 7c
def squaredList(num):
    """Square the input num

    Args:
        num: number (integer or float)

    Returns:
        Number: the input num squared

    Raises:
        TypeError: if num is not a number

    """
    return num * num


# Function to print out all
def applyFuncs(testL, funcList):
    """Print out the results of functions in a list
    Args:
        testL: a list of numbers (integer or float)
        funcList: a list of functions

    Returns:
        None

    Raises:
        TypeError: if testL is a non-number list
        TypeError: if funcList non function list

    """
    for func in funcList:
        lstinit = testL[:]
        applyToEach(lstinit, func)
        print lstinit

# ----
# Test
# ----

testList = [1, -4, 8, -9]
funcs = [mulfive, absList, addone, squaredList]
applyFuncs(testList, funcs)
