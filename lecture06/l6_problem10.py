def howMany(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    num = 0

    for i in range(len(aDict)):
        num += len(aDict.values()[i])

    return num

# ----------
# Test cases
# ----------

animals = {'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')
print howMany(animals)

# -------------------------------
# More test cases from the grader
# -------------------------------

# Test case 1
# -----------
print howMany({})
# Output: 0

# Test case 2
# -----------
print howMany({'i': [20], 'x': [19, 19], 'M': [2, 11], 't': []})
# Output: 5

# Test case 3
# -----------
print howMany({'I': [11, 15, 2, 17], 'U': [11, 20, 17],
              'c': [13, 3, 6], 'J': [6, 1, 2, 20], 'e': [1, 17, 14, 8, 6]})
# Output: 19

# Test case 4
# -----------
print howMany({'j': [12, 11, 12], 'L': [14, 20, 14, 7, 8],
              'U': [1, 13, 20, 15], 'w': [2], 'v': [20, 17], 'x': []})
# Output: 14

# Test case 5
# -----------
print howMany({'i': [11, 9, 16, 8, 18], 'P': [19, 13, 15, 20, 6],
              'G': [4], 'w': [], 'N': [2, 12, 17]})
# Output: 15

# Test case 6
# -----------
print howMany({'e': [15, 16, 20], 'I': [14], 'M': [15, 3, 16],
              'n': [], 'r': [], 'U': [5, 3, 10, 0, 6], 'w': [17, 9]})
# Output: 14

# Test case 7
# -----------
print howMany({'i': [], 'R': [], 'Z': [3, 7, 18, 4, 13],
              'U': [19, 13, 12], 'b': [18]})
# Output: 9

# Test case 8
# -----------
print howMany({'Y': [20, 6]})
# Output: 2

# Test case 9
# -----------
print howMany({'A': [], 'D': [12, 0], 'm': [11, 14, 10, 4],
              'Q': [7, 20, 15], 'p': [7, 4, 20], 't': []})
# Output: 12

# Test case 10
# ------------
print howMany({'E': [16, 11, 13]})
# Output: 3

# -----------------------------------------------------------------------------

# NOTES: Sample answer 1


def howMany1(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many individual values are in the dictionary.
    '''
    result = 0
    for value in aDict.values():
        # Since all the values of aDict are lists, aDict.values() will
        #  be a list of lists
        result += len(value)
    return result

# NOTES: Sample answer 2


def howMany2(aDict):
    '''
    Another way to solve the problem.

    aDict: A dictionary, where all the values are lists.

    returns: int, how many individual values are in the dictionary.
    '''
    result = 0
    for key in aDict.keys():
        result += len(aDict[key])
    return result
