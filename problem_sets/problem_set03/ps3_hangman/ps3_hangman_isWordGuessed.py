def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are
        in lettersGuessed; False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    for letter in secretWord:
        if letter not in lettersGuessed:
            # Return False immidately index of secretWord is not in
            # lettersGuessed list
            return False

    return True

# ----------
# Test cases
# ----------

secretWord = 'apple'
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print isWordGuessed(secretWord, lettersGuessed)

# --------------------------------------
# More test cases from the course grader
# --------------------------------------

# Test 1
# Function call:
print isWordGuessed('apple', ['a', 'e', 'i', 'k', 'p', 'r', 's'])
# Output:
# False

# XXX: Fix Style
# Test 2
# Function call:
print isWordGuessed('durian', ['h', 'a', 'c', 'd', 'i', 'm', 'n', 'r', 't', 'u'])
# Output:
# True

# XXX: Fix Style
# Random Test 1
# Function call:
print isWordGuessed('carrot', ['h', 'x', 'c', 'v', 'y', 'r', 'q', 'd', 'k', 'p'])
# Output:
# False

# XXX: Fix Style
# Random Test 2
# Function call:
print isWordGuessed('lettuce', ['u', 'a', 'k', 'l', 'r', 'd', 'i', 'v', 'b', 'e'])
# Output:
# False

# Random Test 3
# Function call:
print isWordGuessed('lettuce', [])
# Output:
# False

# XXX: Fix Style
# Random Test 4
# Function call:
print isWordGuessed('pineapple', ['z', 'x', 'q', 'p', 'i', 'n', 'e', 'a', 'p', 'p', 'l', 'e'])
# Output:
# True

###############################################################################

# NOTES:

# Alternative answer less efficient

# word = ''

# for letter in secretWord:
#     if letter in lettersGuessed:
#         word += letter

# if word == secretWord:
#     return True
# else:
#     return False
