# 6.00 Problem Set 3
#
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()


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


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...

    guessesLeft = 8
    lettersGuessed = []
    separator = '-------------'

    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is " + \
        str(len(secretWord)) + " letters long."
    print separator

    while guessesLeft > 0:
        print "You have " + str(guessesLeft) + " guesses left."
        print "Available letters: " + getAvailableLetters(lettersGuessed)
        letter = raw_input("Please guess a letter: ").lower()
        if letter in secretWord:
            if letter in lettersGuessed:
                print "Oops! You've already guessed that letter: " + \
                    getGuessedWord(secretWord, lettersGuessed)
                # print 'secretWord: ' + secretWord
                # print 'lettersGuessed: ', lettersGuessed
                print separator
            else:
                lettersGuessed.append(letter)
                print "Good guess: " + \
                    getGuessedWord(secretWord, lettersGuessed)
                # print 'secretWord: ' + secretWord
                # print 'lettersGuessed: ', lettersGuessed
                print separator
        else:
            if letter in lettersGuessed:
                print "Oops! You've already guessed that letter: " + \
                    getGuessedWord(secretWord, lettersGuessed)
                # print 'secretWord: ' + secretWord
                # print 'lettersGuessed: ', lettersGuessed
                print separator
            else:
                lettersGuessed.append(letter)
                print "Oops! That letter is not in my word: " + \
                    getGuessedWord(secretWord, lettersGuessed)
                guessesLeft -= 1
                # print 'secretWord: ' + secretWord
                # print 'lettersGuessed: ', lettersGuessed
                print separator
        if isWordGuessed(secretWord, lettersGuessed):
            # print "Congratulations, you won!"
            return "Congratulations, you won!"
    # print "Sorry, you ran out of guesses. The word was else."
    return "Sorry, you ran out of guesses. The word was else."

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)

# -----------------------------------------------------------
# Test cases used by the grader
# Use them if you wish to test locally with your manual input
# -----------------------------------------------------------

# NOTES: Function call: hangman(c)
# Testing if we can correctly guess a short word...
hangman('c')
# ==> Type and check

# NOTES: Function call: hangman(zzz)
# Testing if we can correctly fill in repeat letters ...
hangman('zzz')
# ==> See if typing 'z' for one time fills 'zzz'

# NOTES: Function call: hangman(c)
# Testing if we can incorrectly guess a short word...
hangman('a')
# [...]
hangman('i')

# NOTES: Function call: hangman(sea)
# Testing if we handle repeat correct guesses...
hangman('sea')
# ==> Checks typing a correct letter does penalise remaining guess count

# NOTES: Function call: hangman(y)
# Testing if we handle repeat incorrect guesses...
hangman('')
# ==> Set any char for secretWord and answer letter non in secretWord

# NOTES: Function call: hangman(zzz)
# Testing if we can correctly fill in repeat letters
#     and handle capitalized input ...
hangman('zzz')
# ==> See if typing 'Z' for one time files 'zzz'

# NOTES: Function call: hangman(y)
# Testing if we handle repeat incorrect guesses...
hangman('y')
# ==> See if typing one same char other than 'y' for consecutively after the
#     first input doesn't penalise the remaining guess counts.

# NOTES: Function call: hangman(camel)
# Testing if we can correctly guess a word...
hangman('camel')
# ==> Type freely and see if any output messages are not contradicting

# NOTES: Function call: hangman(guanabana)
# Testing if we run out of guesses...
hangman('guanabana')
# ==> Type freely and see if any output messages are not contradicting

# NOTES: Function call: hangman(senselessness)
# Testing if we can correctly fill in multiple letters...
hangman('senselessness')
# ==> There are 4 'e's in this secretWord, see if typing 'e' once can correctly
#     produce '_ e_ _ e_ e_ _ _ e_ _ ' and do the same with 's' and so forth

# NOTES: Function call: hangman(cheetah)
# Testing if we correctly handle repeat guesses...
hangman('cheetah')
# ==> Type and test with any chars and any scenarios and see if output messages
#     are not contradicting with chars
