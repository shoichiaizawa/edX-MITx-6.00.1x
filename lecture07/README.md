
Debugging skills
----------------

##### `tests.py`

```python
def isPal(x):
    assert type(x) == list
    temp = x
    temp.reverse
    if temp == x:
        return True
    else:
        return False


def silly(n):
    for i in range(n):
        result = []
        elem = raw_input('Enter element: ')
        result.append(elem)
    if isPal(result):
        print('Yes')
    else:
        print('No')
```

##### In the Python interpreter

```python
>>>
>>> execfile('tests.py')
>>> silly(5)
Enter element: a
Enter element: b
Enter element: c
Enter element: b
Enter element: a
Yes
>>> silly(10)
Enter element: p
Enter element: a
Enter element: l
Enter element: i
Enter element: n
Enter element: n
Enter element: i
Enter element: l
Enter element: a
Enter element: p
Yes
>>> silly(2)
Enter element: a
Enter element: b
Yes
```

##### `tests.py`

Adding a print statement after the for loop in the `silly()` function.

```python
def isPal(x):
    assert type(x) == list
    temp = x
    temp.reverse
    if temp == x:
        return True
    else:
        return False


def silly(n):
    for i in range(n):
        result = []
        elem = raw_input('Enter element: ')
        result.append(elem)
    print(result)
    if isPal(result):
        print('Yes')
    else:
        print('No')
```

##### In the Python interpreter

```python
>>>
>>> execfile('tests.py')
>>> silly(2)
Enter element: a
Enter element: b
['b']
Yes
```

##### `tests.py`

Adding a print statement inside the for loop in the `silly()` function.

```python
def isPal(x):
    assert type(x) == list
    temp = x
    temp.reverse
    if temp == x:
        return True
    else:
        return False


def silly(n):
    for i in range(n):
        result = []
        elem = raw_input('Enter element: ')
        result.append(elem)
        print(result)
    if isPal(result):
        print('Yes')
    else:
        print('No')
```

##### In the Python interpreter

```python
>>>
>>> execfile('tests.py')
>>> silly(2)
Enter element: a
['a']
Enter element: b
['b']
Yes
```

##### `tests.py`

Define the `result` list outside the for loop in the `silly()` function.

```python
def isPal(x):
    assert type(x) == list
    temp = x
    temp.reverse
    if temp == x:
        return True
    else:
        return False


def silly(n):
    result = []
    for i in range(n):
        elem = raw_input('Enter element: ')
        result.append(elem)
        print(result)
    if isPal(result):
        print('Yes')
    else:
        print('No')
```

##### In the Python interpreter

```python
>>>
>>> execfile('tests.py')
>>> silly(2)
Enter element: a
['a']
Enter element: b
['a', 'b']
Yes
```

##### `tests.py`

Add a print statement about in the middle of the `isPal()` function, below the line of `temp.reverse`.

```python
def isPal(x):
    assert type(x) == list
    temp = x
    temp.reverse
    print(temp, x)
    if temp == x:
        return True
    else:
        return False


def silly(n):
    result = []
    for i in range(n):
        elem = raw_input('Enter element: ')
        result.append(elem)
        print(result)
    if isPal(result):
        print('Yes')
    else:
        print('No')
```

##### In the Python interpreter

```python
>>>
>>> execfile('tests.py')
>>> silly(2)
Enter element: a
['a']
Enter element: b
['a', 'b']
(['a', 'b'], ['a', 'b'])
Yes
```

##### `tests.py`

Adding another print statement above the line of `temp.reverse`.

```python
def isPal(x):
    assert type(x) == list
    temp = x
    print(temp, x)
    temp.reverse
    print(temp, x)
    if temp == x:
        return True
    else:
        return False


def silly(n):
    result = []
    for i in range(n):
        elem = raw_input('Enter element: ')
        result.append(elem)
        print(result)
    if isPal(result):
        print('Yes')
    else:
        print('No')
```

##### In the Python interpreter

```python
>>>
>>> execfile('tests.py')
>>> silly(2)
Enter element: a
['a']
Enter element: b
['a', 'b']
(['a', 'b'], ['a', 'b'])
(['a', 'b'], ['a', 'b'])
Yes
```

##### `tests.py`

Replace `temp.reverse` by `temp.reverse()`.

```python
def isPal(x):
    assert type(x) == list
    temp = x
    print(temp, x)
    temp.reverse()
    print(temp, x)
    if temp == x:
        return True
    else:
        return False


def silly(n):
    result = []
    for i in range(n):
        elem = raw_input('Enter element: ')
        result.append(elem)
        print(result)
    if isPal(result):
        print('Yes')
    else:
        print('No')
```

##### In the Python interpreter

```python
>>>
>>> execfile('tests.py')
>>> silly(2)
Enter element: a
['a']
Enter element: b
['a', 'b']
(['a', 'b'], ['a', 'b'])
(['b', 'a'], ['b', 'a'])
Yes
```

##### `tests.py`

Copy `x` using `x[:]` and assign it to `temp`.

```python
def isPal(x):
    assert type(x) == list
    temp = x[:]
    print(temp, x)
    temp.reverse()
    print(temp, x)
    if temp == x:
        return True
    else:
        return False


def silly(n):
    result = []
    for i in range(n):
        elem = raw_input('Enter element: ')
        result.append(elem)
        print(result)
    if isPal(result):
        print('Yes')
    else:
        print('No')
```

##### In the Python interpreter

```python
>>>
>>> execfile('tests.py')
>>> silly(2)
Enter element: a
['a']
Enter element: b
['a', 'b']
(['a', 'b'], ['a', 'b'])
(['b', 'a'], ['a', 'b'])
No
```

Now we obtained the expected results!

### Make sure you test with some other cases previously tested did not work.

##### In the Python interpreter

```python
>>>
>>> silly(5)
Enter element: a
['a']
Enter element: b
['a', 'b']
Enter element: c
['a', 'b', 'c']
Enter element: b
['a', 'b', 'c', 'b']
Enter element: a
['a', 'b', 'c', 'b', 'a']
(['a', 'b', 'c', 'b', 'a'], ['a', 'b', 'c', 'b', 'a'])
(['a', 'b', 'c', 'b', 'a'], ['a', 'b', 'c', 'b', 'a'])
Yes
>>>
>>>
>>> silly(10)
Enter element: p
['p']
Enter element: a
['p', 'a']
Enter element: l
['p', 'a', 'l']
Enter element: i
['p', 'a', 'l', 'i']
Enter element: n
['p', 'a', 'l', 'i', 'n']
Enter element: n
['p', 'a', 'l', 'i', 'n', 'n']
Enter element: i
['p', 'a', 'l', 'i', 'n', 'n', 'i']
Enter element: l
['p', 'a', 'l', 'i', 'n', 'n', 'i', 'l']
Enter element: a
['p', 'a', 'l', 'i', 'n', 'n', 'i', 'l', 'a']
Enter element: p
['p', 'a', 'l', 'i', 'n', 'n', 'i', 'l', 'a', 'p']
(['p', 'a', 'l', 'i', 'n', 'n', 'i', 'l', 'a', 'p'], ['p', 'a', 'l', 'i', 'n', 'n', 'i', 'l', 'a', 'p'])
(['p', 'a', 'l', 'i', 'n', 'n', 'i', 'l', 'a', 'p'], ['p', 'a', 'l', 'i', 'n', 'n', 'i', 'l', 'a', 'p'])
Yes
```
