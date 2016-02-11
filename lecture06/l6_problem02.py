def oddTuples(aTup):
    '''
    aTup: a tuple

    returns: tuple, every other element of aTup.
    '''
    # Your Code Here
    newTup = ()

    for idx, item in enumerate(aTup):
        if idx % 2 == 0:
            newTup += (aTup[idx],)

    return newTup

# ----------
# Test cases
# ----------

print oddTuples(())                                    # ==> ()
print oddTuples((4,))                                  # ==> (4,)
print oddTuples((14, 11, 15, 16, 4))                   # ==> (14, 15, 4)
print oddTuples((7, 10, 4, 15, 9, 19, 6, 5, 10))       # ==> (7, 4, 9, 6, 10)
print oddTuples((5, 3, 8, 9, 11, 18, 14, 4, 16, 1))    # ==> (5, 8, 11, 14, 16)
print oddTuples((2, 7, 12, 7, 2))                      # ==> (2, 12, 2)
print oddTuples((18, 4, 1, 3, 18, 1, 7, 10))           # ==> (18, 1, 18, 7)
print oddTuples((9, 3, 17, 13, 16, 5, 20, 1, 11, 15))  # ==> (9, 17, 16, 20, 11)
print oddTuples((6, 6, 6, 9, 9, 11, 13, 3))            # ==> (6, 6, 9, 13)
print oddTuples((19, 10, 7, 14, 14, 12, 10, 7))        # ==> (19, 7, 14, 10)

# -----------------------------------------------------------------------------

# NOTES: Sample answer 1
#
#
# def oddTuples1(aTup):
#     '''
#     aTup: a tuple
#
#     returns: tuple, every other element of aTup.
#     '''
#     # a placeholder to gather our response
#     rTup = ()
#     index = 0
#
#     # Idea: Iterate over the elements in aTup, counting by 2
#     #  (every other element) and adding that element to
#     #  the result
#     while index < len(aTup):
#         rTup += (aTup[index],)
#         index += 2
#
#     return rTup

# NOTES: Sample answer 2
#
#
# def oddTuples2(aTup):
#     '''
#     Another way to solve the problem.
#
#     aTup: a tuple
#
#     returns: tuple, every other element of aTup.
#     '''
#     # Here is another solution to the problem that uses tuple
#     #  slicing by 2 to achieve the same result
#     return aTup[::2]
