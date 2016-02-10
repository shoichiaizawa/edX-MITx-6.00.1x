Iterative multiplication by successive additions
------------------------------------------------

##### `iterMul.py`

```python
def iterMul(a, b):
    result = 0
    while b > 0:
        result += a
        b -= 1
    return result
```

```python
>>> execfile('iterMul.py')
>>> iterMul(3, 5)
15
>>> iterMul(26, 35)
910
```

--------------------------------------------------------------------------------

Recursive multiplication by successive additions
------------------------------------------------

##### `recMul.py`

```python
def recurMul(a, b):
    if b == 1:
        return a
    else:
        return a + recurMul(a, b-1)
```

```python
>>> execfile('recMul.py')
>>> recurMul(3, 5)
15
>>> recurMul(26, 35)
910
```

--------------------------------------------------------------------------------

Factorial
---------

##### `fact.py`

```python
def factI(n):
    """assumes that n is an int > 0
       returns n!"""
    res = 1
    while n > 1:
        res = res * n
        n -= 1
    return res


def factR(n):
    """assumes that n is an int > 0
       returns n!"""
    if n == 1:
        return n
    return n*factR(n-1)
```

```python
>>> execfile('fact.py')
>>> factI(1)
1
>>> factI(3)
6
>>> factI(25)
15511210043330985984000000L
>>> factR(1)
1
>>> factR(3)
6
>>> factR(25)
15511210043330985984000000L
```

--------------------------------------------------------------------------------

Towers of Hanoi
---------------

##### `towers.py`

```python
def printMove(fr, to):
    print('move from ' + str(fr) + ' to ' + str(to))


def Towers(n, fr, to, spare):
    if n == 1:
        printMove(fr, to)
    else:
        Towers(n-1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(n-1, spare, to, fr)
```

```python
>>> execfile('towers.py')
>>> Towers(1, 'f', 't', 's')
move from f to t
>>> Towers(2, 'f', 't', 's')
move from f to s
move from f to t
move from s to t
>>> Towers(5, 'f', 't', 's')
move from f to t
move from f to s
move from t to s
move from f to t
move from s to f
move from s to t
move from f to t
move from f to s
move from t to s
move from t to f
move from s to f
move from t to s
move from f to t
move from f to s
move from t to s
move from f to t
move from s to f
move from s to t
move from f to t
move from s to f
move from t to s
move from t to f
move from s to f
move from s to t
move from f to t
move from f to s
move from t to s
move from f to t
move from s to f
move from s to t
move from f to t
```

--------------------------------------------------------------------------------

Fibonacci
---------

##### `fib.py`

```python
def fib(x):
    """assumes x an int >= 0
       returns Fibonacci of x"""
    assert type(x) == int and x >= 0
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)
```

```python
>>> execfile('fib.py')
>>> fib(0)
1
>>> fib(1)
1
>>> fib(2)
2
>>> fib(3)
3
>>> fib(4)
5
>>> fib(12)
233
>>> fib(13)
377
>>> fib(15)
987
>>> fib(16)
1597
```

--------------------------------------------------------------------------------

Recursion on non-numerics
-------------------------

##### `isPal.py`

```python
def isPalindrome(s):

    def toChars(s):
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + c
        return ans

    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])

    return isPal(toChars(s))
```

```python
>>> execfile('isPal.py')
>>> isPalindrome('abba')
True
>>> isPalindrome('guttag')
False
>>> isPalindrome('guttug')
True
>>> isPalindrome('Able was I ere I saw Elba')
True
```

--------------------------------------------------------------------------------

Global variables
----------------

##### `fibMetered.py`

```
def fibMetered(x):
    global numCalls
    numCalls += 1
    if x == 0 or x == 1:
        return 1
    else:
        return fibMetered(x-1) + fibMetered(x-2)


def testFib(n):
    for i in range(n+1):
        global numCalls
        numCalls = 0
        print('fib of ' + str(i) + ' = ' + str(fibMetered(i)))
        print('fib called ' + str(numCalls) + ' times')
```

```python
>>>
>>> execfile('fibMetered.py')
>>> testFib(5)
fib of 0 = 1
fib called 1 times
fib of 1 = 1
fib called 1 times
fib of 2 = 2
fib called 3 times
fib of 3 = 3
fib called 5 times
fib of 4 = 5
fib called 9 times
fib of 5 = 8
fib called 15 times
>>>
>>>
>>>
>>> testFib(20)
fib of 0 = 1
fib called 1 times
fib of 1 = 1
fib called 1 times
fib of 2 = 2
fib called 3 times
fib of 3 = 3
fib called 5 times
fib of 4 = 5
fib called 9 times
fib of 5 = 8
fib called 15 times
fib of 6 = 13
fib called 25 times
fib of 7 = 21
fib called 41 times
fib of 8 = 34
fib called 67 times
fib of 9 = 55
fib called 109 times
fib of 10 = 89
fib called 177 times
fib of 11 = 144
fib called 287 times
fib of 12 = 233
fib called 465 times
fib of 13 = 377
fib called 753 times
fib of 14 = 610
fib called 1219 times
fib of 15 = 987
fib called 1973 times
fib of 16 = 1597
fib called 3193 times
fib of 17 = 2584
fib called 5167 times
fib of 18 = 4181
fib called 8361 times
fib of 19 = 6765
fib called 13529 times
fib of 20 = 10946
fib called 21891 times
```
