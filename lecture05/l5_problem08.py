def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    if aStr == '':
        return False
    elif len('aStr') == 1:
        if char == aStr:
            return True
        else:
            return False
    elif char == aStr[len(aStr)/2]:
        return True
    elif char < aStr[len(aStr)/2]:
        return isIn(char, aStr[:len(aStr)/2])
    else:
        return isIn(char, aStr[(len(aStr)/2)+1:])

# ----------
# Test cases
# ----------

print isIn('a', '')                      # ==> False
print isIn('e', 'depvy')                 # ==> True
print isIn('p', 'aabeffllooopprsuuwyz')  # ==> True
print isIn('a', 'adjkpsux')              # ==> True
print isIn('w', 'jknooqqsvv')            # ==> False
print isIn('u', 'aabcmnquuwyyzzz')       # ==> True
print isIn('w', 'ceky')                  # ==> False
print isIn('y', 'abdghikmnnqvvvwxyz')    # ==> True
print isIn('v', 'aadhijkknppsuvvvvz')    # ==> True
print isIn('a', 'fiiikkoptuuvwyy')       # ==> False

# -----------------------------------------------------------------------------

# NOTES: What should your base case be?
#
# You should be thinking about 3 situations:
# - What happens when the string is empty?
# - What happens when the string is of length 1?
# - What happens when the test character equals the middle character?

# NOTES: What should your recursive case be?
#
# You should be thinking about 2 situations:
# - What happens when the test character is smaller than the middle character?
# - What happens when it is larger?

# NOTES: Sample answer
#
#
# def isIn(char, aStr):
#     '''
#     char: a single character
#     aStr: an alphabetized string
#
#     returns: True if char is in aStr; False otherwise
#     '''
#     # Base case: If aStr is empty, we did not find the char.
#     if aStr == '':
#         return False
#
#     # Base case: if aStr is of length 1, just see if the chars are equal
#     if len(aStr) == 1:
#         return aStr == char
#
#     # Base case: See if the character in the middle of aStr equals the
#     # test character
#     midIndex = len(aStr)/2
#     midChar = aStr[midIndex]
#     if char == midChar:
#         # We found the character!
#         return True
#
#     # Recursive case: If the test character is smaller than the middle
#     # character, recursively search on the first half of aStr
#     elif char < midChar:
#         return isIn(char, aStr[:midIndex])
#
#     # Otherwise the test character is larger than the middle character,
#     #  so recursively search on the last half of aStr
#     else:
#         return isIn(char, aStr[midIndex+1:])
