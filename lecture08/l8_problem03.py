def FancyDivide(list_of_numbers, index):
    denom = list_of_numbers[index]
    return [SimpleDivide(item, denom)
            for item in list_of_numbers]


def SimpleDivide(item, denom):
    try:
        return item / denom
    except ZeroDivisionError:
        return 0

# ----------
# Test cases
# ----------

# Test 1:
# -------
print FancyDivide([0, 2, 4], 0)  # ==> [0, 0, 0]

# Test 2:
# -------
print FancyDivide([0, 2, 4], 1)  # ==> [0, 1, 2]

# -----------------------------------------------------------------------------

# NOTES: Sample answer
#
#
# # still takes same arguments
# def SimpleDivide1(item, denom):
#     # start a try-except block
#     try:
#         return item / denom
#     # catch a division by zero and return 0
#     except ZeroDivisionError, e:
#         return 0
