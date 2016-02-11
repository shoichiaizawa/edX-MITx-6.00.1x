def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    num = 0
    ansKey = None

    for i in range(len(aDict)):
        if len(aDict.values()[i]) >= num:
            num = len(aDict.values()[i])
            ansKey = aDict.keys()[i]

    return ansKey

# ----------
# Test cases
# ----------

animals = {'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')
print biggest(animals)

# -------------------------------
# More test cases from the grader
# -------------------------------

# Test case 1
# -----------
print biggest({})
# Output: None

# Test case 2
# -----------
print biggest({'L': []})
# Output: 'L'

# Test case 3
# -----------
print biggest({'a': [17, 19], 'c': [19, 4, 1, 9, 12, 4, 5, 17, 2, 3],
               'b': [2, 2, 19, 0, 7, 14]})
# Output: 'c'

# Test case 4
# -----------
print biggest({'a': [5, 20, 9, 9, 8, 15, 11, 7], 'c': [19, 2, 0, 15, 15, 7],
               'b': [9, 10, 4, 2, 13, 9, 4], 'e': [15, 4], 'd': [17, 12, 18]})
# Output: 'a'

# Test case 5
# -----------
print biggest({'a': [13, 5, 9, 20, 12],
               'b': [15, 13, 17, 18, 4, 6, 11, 15, 7, 8]})
# Output: 'b'

# Test case 6
# -----------
print biggest({'a': [12, 10, 9, 7], 'b': [3, 15]})
# Output: 'a'

# Test case 7
# -----------
print biggest({'a': [8, 11, 12, 9]})
# Output: 'a'

# Test case 8
# -----------
print biggest({'a': [9, 11], 'c': [1], 'b': [14, 14, 6, 11, 4, 13, 12],
               'e': [11, 12, 0, 11, 3], 'd': [8, 0, 18, 8, 3, 3]})
# Output: 'b'

# Test case 9
# -----------
print biggest({'a': [14, 18, 14, 7, 20, 1], 'c': [6, 3, 9, 7],
               'b': [7, 5, 1, 4, 14, 1, 6, 1, 7, 2], 'e': [0], 'd': []})
# Output: 'b'

# Test case 10
# -----------
print biggest({'a': [2], 'c': [4, 7, 6], 'b': [9, 7, 13, 1],
               'e': [20, 5, 15, 2, 4, 16, 4], 'd': [10, 0, 10, 16, 8]})
# Output: 'e'

# -----------------------------------------------------------------------------

# Sample answer 1


def biggest1(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    result = None
    biggestValue = 0
    for key in aDict.keys():
        if len(aDict[key]) >= biggestValue:
            result = key
            biggestValue = len(aDict[key])
    return result
