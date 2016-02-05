def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    user_guess = ''

    for letter in secretWord:
        if letter in lettersGuessed:
            user_guess += letter
        else:
            user_guess += '_ '

    return user_guess

# Test cases:
secretWord = 'apple'
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']     # ==> '_ pp_ e'
print getGuessedWord(secretWord, lettersGuessed)

# --------------------------------------
# More test cases from the course grader
# --------------------------------------

# ------
# Test 1
# ------
# Function call:
getGuessedWord('apple', ['e', 'i', 'k', 'p', 'r', 's'])
# Output:
# '_ pp_ e'

# ------
# Test 2
# ------
# Function call:
getGuessedWord('durian', ['a', 'c', 'd', 'h', 'i', 'm', 'n', 'r', 't', 'u'])
# Output:
# 'durian'

# -------------
# Random Test 1
# -------------
# Function call:
getGuessedWord('coconut', ['n', 'r', 'd', 'h', 'q', 'u', 'z', 'g', 'l', 'a'])
# Output:
# '_ _ _ _ nu_ '

# -------------
# Random Test 2
# -------------
# Function call:
getGuessedWord('banana', ['o', 'q', 'r', 'c', 's', 'n', 'w', 'k', 'j', 'x'])
# Output:
# '_ _ n_ n_ '

# -------------
# Random Test 3
# -------------
# Function call:
getGuessedWord('grapefruit', [])
# Output:
# '_ _ _ _ _ _ _ _ _ _ '

# -------------
# Random Test 4
# -------------
# Function call:
getGuessedWord('pineapple', ['z', 'h', 'b', 'o', 'i', 'y', 't', 'n', 'j', 'r'])
# Output:
# '_ in_ _ _ _ _ _ '
