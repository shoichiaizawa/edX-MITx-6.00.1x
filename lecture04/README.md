Computing powers
----------------

##### `iterativePower.py`

```python
# Example of computation without and with functional abstraction

# Without functional abstraction

x = int(raw_input('Enter a number: '))
p = int(raw_input('Enter an integer power: '))

result = 1

for turn in range(p):
    print('iteration: ' + str(turn) + ' current result: ' + str(result))
    result = result * x


# With functional abstraction


def iterativePower(x, p):
    result = 1
    for turn in range(p):
        print ('iteration: ' + str(turn) + ' current result: ' + str(result))
        result = result * x
    return result
```

Without functional abstraction
------------------------------

```python
>>> # Without functional abstraction
>>> execfile('iterativePower.py')
Enter a number: 3
Enter an integer power: 5
iteration: 0 current result: 1
iteration: 1 current result: 3
iteration: 2 current result: 9
iteration: 3 current result: 27
iteration: 4 current result: 81
```

With functional abstraction
---------------------------

```python
>>> # With functional abstraction
>>> iterativePower(3, 5)
iteration: 0 current result: 1
iteration: 1 current result: 3
iteration: 2 current result: 9
iteration: 3 current result: 27
iteration: 4 current result: 81
243
>>>
>>>
>>> # A function result can be assigned to a variable
>>> z = iterativePower(3, 5)
iteration: 0 current result: 1
iteration: 1 current result: 3
iteration: 2 current result: 9
iteration: 3 current result: 27
iteration: 4 current result: 81
>>> z
243
```

Scoping is local
----------------

```python
>>> # Scoping is local
>>> x = 3
>>> p = 4
>>> result = 5
>>> z = iterativePower(6, 7)
iteration: 0 current result: 1
iteration: 1 current result: 6
iteration: 2 current result: 36
iteration: 3 current result: 216
iteration: 4 current result: 1296
iteration: 5 current result: 7776
iteration: 6 current result: 46656
>>> z
279936
>>> x
3
>>> p
4
>>> result
5
```

--------------------------------------------------------------------------------

Understanding Variable Binding
------------------------------

```python
>>> def f(x):
...     y = 1
...     x = x + y
...     print('x = ' + str(x))
...     return x
...
>>> x = 3
>>> y = 2
>>> z = f(x)
x = 4
>>> z
4
>>> x
3
>>> y
2
```

--------------------------------------------------------------------------------

How Environments Separate Variable Binding
------------------------------------------

##### `twoPower.py`

```python
# From Lecture 4, How Environments Separate Variable Bindings


def square(x):
    return x*x


def twoPower(x, n):
    while n > 1:
        x = square(x)
        n = n/2
    return x
```

```
>>>
>>> execfile('twoPower.py')
>>> square(5)
25
>>>
>>>
>>>
>>> square(4.3)
18.49
>>>
>>>
>>>
>>> twoPower(2, 8)
256
>>>
>>>
>>>
>>> x = 5
>>> n = 1
>>> twoPower(2, 8)
256python
```

--------------------------------------------------------------------------------

Understanding Root Finding
--------------------------

##### `roots.py`

```python
# From Lecture 4, Understanding Root Finding

# root code


def findRoot1(x, power, epsilon):
    low = 0
    high = x
    ans = (high+low)/2.0
    while abs(ans**power - x) > epsilon:
        # print(ans)
        if ans**power < x:
            low = ans
        else:
            high = ans
        ans = (high+low)/2.0
    return ans

# print findRoot1(25.0, 2, .001)
# print findRoot1(27.0, 3, .001)
# print findRoot1(-27.0, 3, .001)


# so can't find cube root of negative number

def findRoot2(x, power, epsilon):
    if x < 0 and power % 2 == 0:
        return None
    # can't find even powered root of negative number
    low = min(0, x)
    high = max(0, x)
    ans = (high+low)/2.0
    while abs(ans**power - x) > epsilon:
        if ans**power < x:
            low = ans
        else:
            high = ans
        ans = (high+low)/2.0
    return ans

# print findRoot2(25.0, 2, .001)
# print findRoot2(27.0, 3, .001)
# print findRoot2(-27.0, 3, .001)
#
# print findRoot2(0.25, 2, .001)
# print findRoot2(-0.125, 3, .001)


def findRoot3(x, power, epsilon):
    if x < 0 and power % 2 == 0:
        return None
    # can't find even powered root of negative number
    low = min(-1.0, x)
    high = max(1.0, x)
    ans = (high+low)/2.0
    while abs(ans**power - x) > epsilon:
        if ans**power < x:
            low = ans
        else:
            high = ans
        ans = (high+low)/2.0
    return ans

# print findRoot3(25.0, 2, .001)
# print findRoot3(27.0, 3, .001)
# print findRoot3(-27.0, 3, .001)
#
# print findRoot3(0.25, 2, .001)
# print findRoot3(-0.125, 3, .001)


def testFindRoot():
    epsilon = 0.0001
    for x in (0.25, -0.25, 2, -2, 8, -8):
        for power in range(1, 4):
            print('Testing x = ' + str(x) +
                  ' and power = ' + str(power))
            res = findRoot3(x, power, epsilon)
            if res == None:
                print('    No root')
            else:
                print('    ' + str(res**power) + ' ~= ' + str(x))
```

```python
>>> findRoot1(25.0, 2, .001)
4.9999237060546875
>>> findRoot1(27.0, 3, .001)
2.999988555908203
>>> findRoot1(-27.0, 3, .001)
^CTraceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "roots.py", line 11, in findRoot1
    if ans**power < x:
KeyboardInterrupt
>>>
```

```python
>>> execfile('roots.py')
>>> findRoot1(-27.0, 3, .001)
-13.5
-20.25
-23.625
-25.3125
-26.15625
-26.578125
-26.7890625
-26.89453125
-26.947265625
-26.9736328125
-26.9868164062
-26.9934082031
-26.9967041016
-26.9983520508
-26.9991760254
-26.9995880127
-26.9997940063
-26.9998970032
-26.9999485016
-26.9999742508
-26.9999871254
-26.9999935627
-26.9999967813
-26.9999983907
-26.9999991953
-26.9999995977
-26.9999997988
-26.9999998994
-26.9999999497
-26.9999999749
-26.9999999874
-26.9999999937
-26.9999999969
-26.9999999984
-26.9999999992
-26.9999999996
-26.9999999998
-26.9999999999
-27.0
-27.0
-27.0
[...]
-27.0
-27.0
-27.0
^C7.0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "roots.py", line 11, in findRoot1
    print(ans)
KeyboardInterrupt
```

```python
>>> findRoot2(-27.0, 3, .001)
-2.999988555908203
>>> findRoot2(0.25, 2, .001)
^CTraceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "roots.py", line 33, in findRoot2
    while abs(ans**power - x) > epsilon:
KeyboardInterrupt
```

```python
>>> findRoot3(0.25, 2, .001)
0.5
>>> findRoot3(-0.25, 2, .001)
>>> findRoot3(0.25, 3, .001)
0.6298828125
>>> findRoot3(-0.25, 3, .001)
-0.6298828125
>>> findRoot3(25.0, 2, .001)
4.9999237060546875
>>> findRoot3(-27.0, 3, .001)
-2.9999847412109375
```

--------------------------------------------------------------------------------

Modules
-------

##### `circle.py`

```python
# circle.py
# From Lecture 4, Modules

pi = 3.14159


def area(radius):
    return pi*(radius**2)


def circumference(radius):
    return 2*pi*radius
```

```python
>>> import circle
>>> pi = 3.0
>>> print(pi)
3.0
>>> print(circle.pi)
3.14159
>>> circle.area(3.0)
28.27431
>>>
>>>
>>>
>>> from circle import *
>>> pi = 0.0
>>> pi
0.0
>>> area(3)
28.27431
>>> circle.pi
3.14159
```
