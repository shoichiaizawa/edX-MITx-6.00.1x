Exceptions
----------

##### `execeptionsCode.py`

```python
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError, e:
        print "division by zero! " + str(e)
    else:
        print "result is", result
    finally:
        print "executing finally clause"


def divideNew(x, y):
    try:
        result = x / y
    except ZeroDivisionError, e:
        print "division by zero! " + str(e)
    except TypeError:
        divideNew(int(x), int(y))
    else:
        print "result is", result
    finally:
        print "executing finally clause"
```

##### In the Python interpreter

```python
>>>
>>> execfile('exceptionsCode.py')
>>> divide(3, 4)
result is 0
executing finally clause
>>> divide(3, 0)
division by zero! integer division or modulo by zero
executing finally clause
>>> divide('3', '4')
executing finally clause
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "exceptionsCode.py", line 3, in divide
    result = x / y
TypeError: unsupported operand type(s) for /: 'str' and 'str'
>>>
>>>
>>> divideNew(3, 4)
result is 0
executing finally clause
>>> divideNew(3, 0)
division by zero! integer division or modulo by zero
executing finally clause
>>> divideNew('3', '4')
result is 0
executing finally clause
executing finally clause
```

--------------------------------------------------------------------------------

An example of exceptions
------------------------

##### `subjectCode.py`

```python
def getSubjectStats(subject, weights):
    return [[elt[0], elt[1], avg(elt[1], weights)]
            for elt in subject]


def dotProduct(a, b):
    result = 0.0
    for i in range(len(a)):
        result += a[i]*b[i]
    return result


def avg(grades, weights):
    return dotProduct(grades, weights)/len(grades)


test = [[['fred', 'flintstone'], [10.0, 5.0, 85.0]],
        [['barney', 'rubble'], [10.0, 8.0, 74.0]],
        [['wilma', 'flintstone'], [8.0, 10.0, 96.0]],
        [['dino'], []]]

weights = [.3, .2, .5]

weights1 = [.15, .1, .25, .25]

test1 = [[['fred', 'flintstone'], [10.0, 5.0, 85.0, 'D']],
         [['barney', 'rubble'], [10.0, 8.0, 74.0, 'B']],
         [['wilma', 'flintstone'], [8.0, 10.0, 96.0, 'A']],
         [['dino'], []]]

test2 = [[['fred', 'flintstone'], [10.0, 5.0, 8500, 'D']],
         [['barney', 'rubble'], [10.0, 8.0, 74.0, 'B']],
         [['wilma', 'flintstone'], [8.0, 10.0, 96.0, 'A']]]
```

##### In the Python interpreter

```python
>>>
>>> execfile('subjectCode.py')
>>> getSubjectStats(test, weights)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "subjectCode.py", line 3, in getSubjectStats
    for elt in subject]
  File "subjectCode.py", line 14, in avg
    return dotProduct(grades, weights)/len(grades)
ZeroDivisionError: float division by zero
```

##### `subjectCode.py`

```python
def getSubjectStats(subject, weights):
    return [[elt[0], elt[1], avg(elt[1], weights)]
            for elt in subject]


def dotProduct(a, b):
    result = 0.0
    for i in range(len(a)):
        result += a[i]*b[i]
    return result


# def avg(grades, weights):
#     return dotProduct(grades, weights)/len(grades)


def avg(grades, weights):
    try:
        return dotProduct(grades, weights)/len(grades)
    except ZeroDivisionError:
        print 'no grades data'


test = [[['fred', 'flintstone'], [10.0, 5.0, 85.0]],
        [['barney', 'rubble'], [10.0, 8.0, 74.0]],
        [['wilma', 'flintstone'], [8.0, 10.0, 96.0]],
        [['dino'], []]]

weights = [.3, .2, .5]

weights1 = [.15, .1, .25, .25]

test1 = [[['fred', 'flintstone'], [10.0, 5.0, 85.0, 'D']],
         [['barney', 'rubble'], [10.0, 8.0, 74.0, 'B']],
         [['wilma', 'flintstone'], [8.0, 10.0, 96.0, 'A']],
         [['dino'], []]]

test2 = [[['fred', 'flintstone'], [10.0, 5.0, 8500, 'D']],
         [['barney', 'rubble'], [10.0, 8.0, 74.0, 'B']],
         [['wilma', 'flintstone'], [8.0, 10.0, 96.0, 'A']]]

```

##### In the Python interpreter

```python
>>> execfile('subjectCode.py')
>>> getSubjectStats(test, weights)
no grades data
[[['fred', 'flintstone'], [10.0, 5.0, 85.0], 15.5], [['barney', 'rubble'], [10.0, 8.0, 74.0], 13.866666666666667], [['wilma', 'flintstone'], [8.0, 10.0, 96.0], 17.466666666666665], [['dino'], [], None]]
```

--------------------------------------------------------------------------------

Exceptions as Control Flow
--------------------------

--------------------------------------------------------------------------------

Assertions
----------

