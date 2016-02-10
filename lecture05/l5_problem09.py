def semordnilapWrapper(str1, str2):
    # A single-length string cannot be semordnilap
    if len(str1) == 1 or len(str2) == 1:
        return False

    # Equal strings cannot be semordnilap
    if str1 == str2:
        return False

    return semordnilap(str1, str2)


def semordnilap(str1, str2):
    '''
    str1: a string
    str2: a string

    returns: True if str1 and str2 are semordnilap;
             False otherwise.
    '''
    # Your code here
    if len(str1) != len(str2):
        return False
    elif len(str1) == 1 and len(str2) == 1:
        if str1 == str2:
            return True
        else:
            return False
    elif str1[0] == str2[-1]:
        return semordnilap(str1[1:], str2[:-1])

# ----------
# Test cases
# ----------

print semordnilapWrapper('nametag', 'gateman')
print semordnilapWrapper('dog', 'god')
print semordnilapWrapper('live', 'evil')
print semordnilapWrapper('desserts', 'stressed')

# -------------------------------
# More test cases from the grader
# -------------------------------

print semordnilapWrapper('live', 'evil')                  # ==> True
print semordnilapWrapper('tact', 'cat')                   # ==> False
print semordnilapWrapper('desserts', 'stressed')          # ==> True
print semordnilapWrapper('level', 'level')                # ==> False
print semordnilapWrapper('semordnilap', 'palindrome')     # ==> False
print semordnilapWrapper('rats live on', 'no evil star')  # ==> True
print semordnilapWrapper('mkwlfdgnouivbqh', 'gazwcj')     # ==> False
print semordnilapWrapper('brjkzv', 'qalpifsxtgwvcu')      # ==> False
print semordnilapWrapper('mopqfrxnvi', 'ncwevyhozdf')     # ==> False
print semordnilapWrapper('p', 'q')                        # ==> False
print semordnilapWrapper('h', 'h')                        # ==> False

# -----------------------------------------------------------------------------

# # NOTES: Sample answer
#
#
# def semordnilapWrapper(str1, str2):
#     # A single-length string cannot be semordnilap
#     if len(str1) == 1 or len(str2) == 1:
#         return False
#
#     # Equal strings cannot be semordnilap
#     if str1 == str2:
#         return False
#
#     return semordnilap(str1, str2)
#
#
# def semordnilap(str1, str2):
#     '''
#     str1: a string
#     str2: a string
#
#     returns: True if str1 and str2 are semordnilap;
#              False otherwise.
#     '''
#     # If strings aren't the same length, they cannot be semordnilap
#     if len(str1) != len(str2):
#         return False
#
#     # Base case: if the strings are each of length 1, check if they're equal
#     if len(str1) == 1:
#         return str1 == str2
#
#     # Recursive case: check if the first letter of str1 equals the last letter
#     # of str2
#     if str1[0] == str2[-1]:
#         return semordnilap(str1[1:], str2[:-1])
#     else:
#         return False
