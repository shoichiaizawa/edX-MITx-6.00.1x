def lenRecur(aStr):
    '''
    aStr: a string

    returns: int, the length of aStr
    '''
    # Your code here
    if aStr == '':
        return 0
    elif aStr != '':
        return 1 + lenRecur(aStr[:-1])

# ----------
# Test cases
# ----------

print lenRecur('')                     # ==> 0
print lenRecur('meswotlknjxyk')        # ==> 13
print lenRecur('udzymfmblamtnpl')      # ==> 15
print lenRecur('kepcyen')              # ==> 7
print lenRecur('pipsg')                # ==> 5
print lenRecur('ltlcxgmay')            # ==> 9
print lenRecur('n')                    # ==> 1
print lenRecur('iucywnoatsdgxqmugre')  # ==> 19
