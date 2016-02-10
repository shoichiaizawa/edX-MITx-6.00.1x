def lenIter(aStr):
    '''
    aStr: a string

    returns: int, the length of aStr
    '''
    # Your code here
    num = 0

    for i in aStr:
        num += 1

    return num

# ----------
# Test cases
# ----------

print lenIter('')                    # ==> 0
print lenIter('qtyqgvqxbhdny')       # ==> 13
print lenIter('xhbmxgo')             # ==> 7
print lenIter('sijeyib')             # ==> 7
print lenIter('qnoldtqqhxslouzjca')  # ==> 18
print lenIter('kjwcydkdbkcx')        # ==> 12
print lenIter('gyziprimsjodbadl')    # ==> 16
print lenIter('egwjhw')              # ==> 6
