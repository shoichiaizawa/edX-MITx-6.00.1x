def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])


# -----------------
# Examples Question
# -----------------

testList = [1, -4, 8, -9]


def mulfive(num):
    return num * 5

applyToEach(testList, mulfive)
print testList


# -------------
# L6 Problem 7a
# -------------

testList = [1, -4, 8, -9]


def absList(num):
    return abs(num)

applyToEach(testList, absList)
print testList


# -------------
# L6 Problem 7b
# -------------

testList = [1, -4, 8, -9]


def addone(num):
    return num + 1

applyToEach(testList, addone)
print testList

# -------------
# L6 Problem 7c
# -------------

testList = [1, -4, 8, -9]


def squaredList(num):
    return num * num

applyToEach(testList, squaredList)
print testList

# -------------------------------------------------------
# Printing out all in one with a function with a for loop
# -------------------------------------------------------

funcs = [mulfive, absList, addone, squaredList]


def applyFuncs(funcList):
    for func in funcList:
        testList = [1, -4, 8, -9]
        applyToEach(testList, func)
        print testList

applyFuncs(funcs)
