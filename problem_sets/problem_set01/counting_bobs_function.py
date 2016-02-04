def subStrFinder(s, subStr):
    """Find the number of sub-strings subStr in the main string s

    Args:
        s: the main string to be searched if how many times
           sub-string subStr found in it
        subStr: the sub-substring to be searched in the main string s

    Returns:
        the number of sub-strings subStr found in the main string s

    Raises:
        TypeError: if s is not a string
        TypeError: if subStr is not a string
    """
    count = 0
    for idx, item in enumerate(s):
        if s[idx:idx+len(subStr)] == subStr:
            count += 1

    return count

    # print 'Number of times bob occurs is: ' + str(count)
    # print "Number of times the sub-string '" + subStr + \
    #       "' found in the string '" + s + "' is: " + str(count)


# Test the function:
print subStrFinder('azcbobobegghakl', 'bob')
# print 'Number of times bob occurs is: ' + str(subStrFinder(s, 'bob'))
