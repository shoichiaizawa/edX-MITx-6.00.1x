import string


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    alphabets = string.ascii_lowercase

    for letter in lettersGuessed:
        if letter in alphabets:
            alphabets = alphabets.replace(letter, '')

    return alphabets

# -----------
# Test cases:
# -----------

lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print getAvailableLetters(lettersGuessed)   # ==> abcdfghjlmnoqtuvwxyz

# --------------------------------------
# More test cases from the course grader
# --------------------------------------

# ------
# Test 1
# ------
# Function call:
print getAvailableLetters(['e', 'i', 'k', 'p', 'r', 's'])
# Output:
# 'abcdfghjlmnoqtuvwxyz'

# ------
# Test 2
# ------
# Function call:
print getAvailableLetters([])
# Output:
# 'abcdefghijklmnopqrstuvwxyz'

# -------------
# Random Test 1
# -------------
# Function call:
print getAvailableLetters(['s', 'r', 'n', 'v'])
# Output:
# 'abcdefghijklmopqtuwxyz'

# -------------
# Random Test 2
# -------------
# Function call:
print getAvailableLetters(['r', 'x', 'k', 'o', 'y', 'n', 'i', 'g'])
# Output:
# 'abcdefhjlmpqstuvwz'

# -------------
# Random Test 3
# -------------
# Function call:
print getAvailableLetters(['a', 'j', 'k', 'm', 'o', 'w', 'r'])
# Output:
# 'bcdefghilnpqstuvxyz'

# -------------
# Random Test 4
# -------------
# Function call:
print getAvailableLetters(['t'])
# Output:
# 'abcdefghijklmnopqrsuvwxyz'

###############################################################################

# NOTES

# >>> import string
# >>> print string.ascii_lowercase
# abcdefghijklmnopqrstuvwxyz
