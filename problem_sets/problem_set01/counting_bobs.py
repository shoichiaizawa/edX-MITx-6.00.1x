# Solution without a function
s = 'azcbobobegghakl'
bob_count = 0
bob = 'bob'

for idx, item in enumerate(s):
    #  print 'Iteration:', idx
    if s[idx:idx+3] == bob:
        #  print 'Print from index', idx, 'to', idx+3
        #  print s[idx:idx+3]
        bob_count += 1

print 'Number of times bob occurs is: ' + str(bob_count)


#  # Solution with a function
#  s = 'azcbobobegghakl'


#  def subStrFinder(s, subStr):
#      """Find the number of sub-strings subStr in the main string s

#      Args:
#          s: the main string to be searched if how many times
#             sub-string subStr found in it
#          subStr: the sub-substring to be searched in the main string s

#      Returns:
#          the number of sub-strings subStr found in the main string s

#      Raises:
#          TypeError: if s is not a string
#          TypeError: if subStr is not a string
#      """
#      count = 0
#      for idx, item in enumerate(s):
#          if s[idx:idx+len(subStr)] == subStr:
#              count += 1
#      return count

#  #  Test the function:
#  print 'Number of times bob occurs is: ' + str(subStrFinder(s, 'bob'))
