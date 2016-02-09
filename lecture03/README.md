Finding a cube root of an integer
---------------------------------

##### `lectureCode_lec3.2.4.py`

```python
# lecture 3.2, slide 4

# Find the cube root of a perfect cube
x = int(raw_input('Enter an integer: '))
ans = 0
while ans**3 < x:
    ans = ans + 1
if ans**3 != x:
    print(str(x) + ' is not a perfect cube')
else:
    print('Cube root of ' + str(x) + ' is ' + str(ans))
```

```python
>>> execfile('lectureCode_lec3.2.4.py')
Enter an integer: 27
Cube root of 27 is 3
>>> execfile('lectureCode_lec3.2.4.py')
Enter an integer: 24
24 is not a perfect cube
>>> execfile('lectureCode_lec3.2.6.py')
```

Extending scope
---------------

##### `lectureCode_lec3.2.6.py`

```python
# lecture 3.2, slide 6

# Find the cube root of a perfect cube
x = int(raw_input('Enter an integer: '))
ans = 0
while ans**3 < abs(x):
    ans = ans + 1
if ans**3 != abs(x):
    print(str(x) + ' is not a perfect cube')
else:
    if x < 0:
        ans = -ans
    print('Cube root of ' + str(x) + ' is ' + str(ans))
```

```python
Enter an integer: 27
Cube root of 27 is 3
>>> execfile('lectureCode_lec3.2.6.py')
Enter an integer: -27
Cube root of -27 is -3
```

What happens if we miss a condition?
------------------------------------

### Suppose we don't initialise the variable?

Remove `ans = 0`

##### `lectureCode_lec3.2.6.py`

```python
# lecture 3.2, slide 6

# Find the cube root of a perfect cube
x = int(raw_input('Enter an integer: '))
# ans = 0
while ans**3 < abs(x):
    ans = ans + 1
if ans**3 != abs(x):
    print(str(x) + ' is not a perfect cube')
else:
    if x < 0:
        ans = -ans
    print('Cube root of ' + str(x) + ' is ' + str(ans))
```

```python
>>> execfile('lectureCode_lec3.2.6.py')
Enter an integer: 27
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
  File "lectureCode_lec3.2.6.py", line 6, in <module>
    while ans**3 < abs(x):
NameError: name 'ans' is not defined
```

### Suppose we don't change the variable inside the loop?

Remove `ans = ans + 1`

##### `lectureCode_lec3.2.6.py`

```python
# lecture 3.2, slide 6

# Find the cube root of a perfect cube
x = int(raw_input('Enter an integer: '))
ans = 0
while ans**3 < abs(x):
    # ans = ans + 1
    print(ans)
if ans**3 != abs(x):
    print(str(x) + ' is not a perfect cube')
else:
    if x < 0:
        ans = -ans
    print('Cube root of ' + str(x) + ' is ' + str(ans))
```

```python
>>> execfile('lectureCode_lec3.2.6.py')
Enter an integer: 27
0
0
0
[...]
0
0
0
^C
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "lectureCode_lec3.2.6.py", line 8, in <module>
    print(ans)
KeyboardInterrupt
>>>
```

--------------------------------------------------------------------------------

A cleaned up cube root finder using a for loop
----------------------------------------------

##### `lectureCode_lec3.3.3.py`

```python
# lecture 3.3, slide 3

# Find the cube root of a perfect cube
x = int(raw_input('Enter an integer: '))
for ans in range(0, abs(x)+1):
    if ans**3 == abs(x):
        break
if ans**3 != abs(x):
    print(str(x) + ' is not a perfect cube')
else:
    if x < 0:
        ans = -ans
    print('Cube root of ' + str(x) + ' is ' + str(ans))
```

```python
>>> execfile('lectureCode_lec3.3.3.py')
Enter an integer: 27
Cube root of 27 is 3
>>> execfile('lectureCode_lec3.3.3.py')
Enter an integer: -27
Cube root of -27 is -3
>>> execfile('lectureCode_lec3.3.3.py')
Enter an integer: 12345
12345 is not a perfect cube
>>>
```

--------------------------------------------------------------------------------

Converting decimal integer to binary
------------------------------------

##### `lectureCode_lec3.4.3.py`

```python
# lecture 3.4, slide 3

num = 302
# num = 256

if num < 0:
    isNeg = True
    num = abs(num)
else:
    isNeg = False
result = ''
if num == 0:
    result = '0'
while num > 0:
    result = str(num%2) + result
    num = num/2
if isNeg:
    result = '-' + result
```

```python
>>> # num = 302
>>> execfile('lectureCode_lec3.4.3.py')
>>> result
'100101110'
>>>
>>>
>>>
>>> # num = 256
>>> execfile('lectureCode_lec3.4.3.py')
>>> result
'100000000'
>>>
```

So what about fractions?
------------------------

##### `lectureCode_lec3.4.4.py`

```python
# lecture 3.4, slide 4

x = float(raw_input('Enter a decimal number between 0 and 1: '))

p = 0
while ((2**p)*x)%1 != 0:
    print('Remainder = ' + str((2**p)*x - int((2**p)*x)))
    p += 1

num = int(x*(2**p))

result = ''
if num == 0:
    result = '0'
while num > 0:
    result = str(num%2) + result
    num = num/2

for i in range(p - len(result)):
    result = '0' + result

result = result[0:-p] + '.' + result[-p:]
print('The binary representation of the decimal ' + str(x) + ' is ' + str(result))
```

```python>>> execfile('lectureCode_lec3.4.3.py')
>>> execfile('lectureCode_lec3.4.4.py')
Enter a decimal number between 0 and 1: .375
Remainder = 0.375
Remainder = 0.75
Remainder = 0.5
The binary representation of the decimal 0.375 is .011
>>>
>>>
>>>
>>> execfile('lectureCode_lec3.4.4.py')
Enter a decimal number between 0 and 1: .1
Remainder = 0.1
Remainder = 0.2
Remainder = 0.4
Remainder = 0.8
Remainder = 0.6
Remainder = 0.2
Remainder = 0.4
Remainder = 0.8
Remainder = 0.6
Remainder = 0.2
Remainder = 0.4
Remainder = 0.8
Remainder = 0.6
Remainder = 0.2
Remainder = 0.4
Remainder = 0.8
Remainder = 0.6
Remainder = 0.200000000001
Remainder = 0.400000000001
Remainder = 0.800000000003
Remainder = 0.600000000006
Remainder = 0.200000000012
Remainder = 0.400000000023
Remainder = 0.800000000047
Remainder = 0.600000000093
Remainder = 0.200000000186
Remainder = 0.400000000373
Remainder = 0.800000000745
Remainder = 0.60000000149
Remainder = 0.20000000298
Remainder = 0.40000000596
Remainder = 0.800000011921
Remainder = 0.600000023842
Remainder = 0.200000047684
Remainder = 0.400000095367
Remainder = 0.800000190735
Remainder = 0.60000038147
Remainder = 0.200000762939
Remainder = 0.400001525879
Remainder = 0.800003051758
Remainder = 0.600006103516
Remainder = 0.200012207031
Remainder = 0.400024414062
Remainder = 0.800048828125
Remainder = 0.60009765625
Remainder = 0.2001953125
Remainder = 0.400390625
Remainder = 0.80078125
Remainder = 0.6015625
Remainder = 0.203125
Remainder = 0.40625
Remainder = 0.8125
Remainder = 0.625
Remainder = 0.25
Remainder = 0.5
The binary representation of the decimal 0.1 is .0001100110011001100110011001100110011001100110011001101
```

--------------------------------------------------------------------------------

Exhaustive enumeration
----------------------

##### `lectureCode_lec3.5.2.py`

```python
# lecture 3.5, slide 2

x = 25
# x = 12345
epsilon = 0.01
step = epsilon**2
# step = .5
# step = 2
numGuesses = 0
ans = 0.0
while (abs(ans**2 - x)) >= epsilon and ans <= x:
    ans += step
    numGuesses += 1
print('numGuesses = ' + str(numGuesses))
if abs(ans**2-x) >= epsilon:
    print('Failed on square root of ' + str(x))
else:
    print(str(ans) + ' is close to the square root of ' + str(x))
```

```python
>>> # x = 25, step = epsilon**2 where epsilon = 0.01
>>> execfile('lectureCode_lec3.5.2.py')
numGuesses = 49990
4.999 is close to the square root of 25
>>>
>>>
>>> # x = 25, step = 0.5
>>> execfile('lectureCode_lec3.5.2.py')
numGuesses = 10
5.0 is close to the square root of 25
>>>
>>>
>>> # x = 25, step = 2
>>> execfile('lectureCode_lec3.5.2.py')
numGuesses = 13
Failed on square root of 25
>>>
>>>
>>> # x = 12345, step = epsilon**2 where epsilon = 0.01
>>> execfile('lectureCode_lec3.5.2.py')
numGuesses = 1111081
111.108100003 is close to the square root of 12345
```

--------------------------------------------------------------------------------

Bisection search
----------------

##### `lectureCode_lec3.6.2.py`

```python
# lecture 3.6, slide 2
# bisection search for square root

x = 25
# x = 12345
# x = 1234567
epsilon = 0.01
numGuesses = 0
low = 0.0
high = x
ans = (high + low)/2.0
while abs(ans**2 - x) >= epsilon:
    print('low = ' + str(low) + ' high = ' + str(high) + ' ans = ' + str(ans))
    numGuesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
print('numGuesses = ' + str(numGuesses))
print(str(ans) + ' is close to square root of ' + str(x))
```

```python$
>>> # x = 25
KeyboardInterrupt
>>> execfile('lectureCode_lec3.6.2.py')
low = 0.0 high = 25 ans = 12.5
low = 0.0 high = 12.5 ans = 6.25
low = 0.0 high = 6.25 ans = 3.125
low = 3.125 high = 6.25 ans = 4.6875
low = 4.6875 high = 6.25 ans = 5.46875
low = 4.6875 high = 5.46875 ans = 5.078125
low = 4.6875 high = 5.078125 ans = 4.8828125
low = 4.8828125 high = 5.078125 ans = 4.98046875
low = 4.98046875 high = 5.078125 ans = 5.029296875
low = 4.98046875 high = 5.029296875 ans = 5.0048828125
low = 4.98046875 high = 5.0048828125 ans = 4.99267578125
low = 4.99267578125 high = 5.0048828125 ans = 4.99877929688
low = 4.99877929688 high = 5.0048828125 ans = 5.00183105469
numGuesses = 13
5.00030517578 is close to square root of 25
>>>
>>>
>>> # x = 12345
>>> execfile('lectureCode_lec3.6.2.py')
low = 0.0 high = 12345 ans = 6172.5
low = 0.0 high = 6172.5 ans = 3086.25
low = 0.0 high = 3086.25 ans = 1543.125
low = 0.0 high = 1543.125 ans = 771.5625
low = 0.0 high = 771.5625 ans = 385.78125
low = 0.0 high = 385.78125 ans = 192.890625
low = 0.0 high = 192.890625 ans = 96.4453125
low = 96.4453125 high = 192.890625 ans = 144.66796875
low = 96.4453125 high = 144.66796875 ans = 120.556640625
low = 96.4453125 high = 120.556640625 ans = 108.500976562
low = 108.500976562 high = 120.556640625 ans = 114.528808594
low = 108.500976562 high = 114.528808594 ans = 111.514892578
low = 108.500976562 high = 111.514892578 ans = 110.00793457
low = 110.00793457 high = 111.514892578 ans = 110.761413574
low = 110.761413574 high = 111.514892578 ans = 111.138153076
low = 110.761413574 high = 111.138153076 ans = 110.949783325
low = 110.949783325 high = 111.138153076 ans = 111.043968201
low = 111.043968201 high = 111.138153076 ans = 111.091060638
low = 111.091060638 high = 111.138153076 ans = 111.114606857
low = 111.091060638 high = 111.114606857 ans = 111.102833748
low = 111.102833748 high = 111.114606857 ans = 111.108720303
low = 111.102833748 high = 111.108720303 ans = 111.105777025
low = 111.105777025 high = 111.108720303 ans = 111.107248664
low = 111.107248664 high = 111.108720303 ans = 111.107984483
low = 111.107984483 high = 111.108720303 ans = 111.108352393
low = 111.107984483 high = 111.108352393 ans = 111.108168438
numGuesses = 26
111.108076461 is close to square root of 12345
>>>
>>>
>>> x = 1234567
>>> execfile('lectureCode_lec3.6.2.py')
low = 0.0 high = 1234567 ans = 617283.5
low = 0.0 high = 617283.5 ans = 308641.75
low = 0.0 high = 308641.75 ans = 154320.875
low = 0.0 high = 154320.875 ans = 77160.4375
low = 0.0 high = 77160.4375 ans = 38580.21875
low = 0.0 high = 38580.21875 ans = 19290.109375
low = 0.0 high = 19290.109375 ans = 9645.0546875
low = 0.0 high = 9645.0546875 ans = 4822.52734375
low = 0.0 high = 4822.52734375 ans = 2411.26367188
low = 0.0 high = 2411.26367188 ans = 1205.63183594
low = 0.0 high = 1205.63183594 ans = 602.815917969
low = 602.815917969 high = 1205.63183594 ans = 904.223876953
low = 904.223876953 high = 1205.63183594 ans = 1054.92785645
low = 1054.92785645 high = 1205.63183594 ans = 1130.27984619
low = 1054.92785645 high = 1130.27984619 ans = 1092.60385132
low = 1092.60385132 high = 1130.27984619 ans = 1111.44184875
low = 1092.60385132 high = 1111.44184875 ans = 1102.02285004
low = 1102.02285004 high = 1111.44184875 ans = 1106.7323494
low = 1106.7323494 high = 1111.44184875 ans = 1109.08709908
low = 1109.08709908 high = 1111.44184875 ans = 1110.26447392
low = 1110.26447392 high = 1111.44184875 ans = 1110.85316133
low = 1110.85316133 high = 1111.44184875 ans = 1111.14750504
low = 1110.85316133 high = 1111.14750504 ans = 1111.00033319
low = 1111.00033319 high = 1111.14750504 ans = 1111.07391912
low = 1111.07391912 high = 1111.14750504 ans = 1111.11071208
low = 1111.07391912 high = 1111.11071208 ans = 1111.0923156
low = 1111.0923156 high = 1111.11071208 ans = 1111.10151384
low = 1111.10151384 high = 1111.11071208 ans = 1111.10611296
low = 1111.10611296 high = 1111.11071208 ans = 1111.10841252
low = 1111.10841252 high = 1111.11071208 ans = 1111.1095623
low = 1111.1095623 high = 1111.11071208 ans = 1111.11013719
low = 1111.11013719 high = 1111.11071208 ans = 1111.11042464
low = 1111.11042464 high = 1111.11071208 ans = 1111.11056836
low = 1111.11056836 high = 1111.11071208 ans = 1111.11064022
low = 1111.11064022 high = 1111.11071208 ans = 1111.11067615
low = 1111.11067615 high = 1111.11071208 ans = 1111.11069412
numGuesses = 36
1111.1107031 is close to square root of 1234567
```

--------------------------------------------------------------------------------

Newton-Raphson
--------------

[Newton's method](https://en.wikipedia.org/wiki/Newton%27s_method)

##### `lectureCode_lec3.7.3.py`

```python
# Lecture 3.7, slide 3

# Newton-Raphson for square root

epsilon = 0.01
y = 24.0
guess = y/2.0

while abs(guess*guess - y) >= epsilon:
    guess = guess - (((guess**2) - y)/(2*guess))
    print(guess)
print('Square root of ' + str(y) + ' is about ' + str(guess))
```

```python
>>> # y = 24.0
>> execfile('lectureCode_lec3.7.3.py')
7.0
5.21428571429
4.90851272016
4.89898874321
Square root of 24.0 is about 4.89898874321
>>>
>>>
>>> # y = 25.0
>>> execfile('lectureCode_lec3.7.3.py')
7.25
5.34913793103
5.01139410653
5.00001295305
Square root of 25.0 is about 5.00001295305
>>>
>>>
>>> # y = 12345.0
>>> execfile('lectureCode_lec3.7.3.py')
3087.25
1545.62435217
776.805707886
396.348856318
213.747829978
135.75140114
113.344844521
111.130126324
111.108057705
Square root of 12345.0 is about 111.108057705
```
