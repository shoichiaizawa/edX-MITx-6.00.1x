Tuples
------

```python
>>>
>>> t1 = (1, 'two', 3)
>>> print(t1)
(1, 'two', 3)
>>> t1
(1, 'two', 3)
>>> t2 = (t1, 'four')
>>> t2
((1, 'two', 3), 'four')
>>>
>>>
>>> t1 + t2
(1, 'two', 3, (1, 'two', 3), 'four')
>>>
>>>
>>> (t1 + t2)[3]
(1, 'two', 3)
>>>
>>>
>>> (t1 + t2)[2:5]
(3, (1, 'two', 3), 'four')
>>>
>>>
>>> t3 = ('five',)
>>> t1 + t2 + t3
(1, 'two', 3, (1, 'two', 3), 'four', 'five')
>>> (3)
3
>>> (3,)
(3,)
```

```python
>> execfile('divisors.py')
42
>>> findDivisors(20, 100)
(1, 2, 4, 5, 10, 20)
>>>
>>>
>>> divs = findDivisors(20, 100)
>>> total = 0
>>> for d in divs:
...     total += d
...
>>> total
42
```

--------------------------------------------------------------------------------

List
----

```python
>>>
>>> Techs = ['MIT', 'Cal Tech']
>>> Ivys = ['Harvard', 'Yale', 'Brown']
>>> Techs
['MIT', 'Cal Tech']
>>> Ivys[1]
'Yale'
>>> Ivys[:2]
['Harvard', 'Yale']
>>>
>>>
>>> Univs = [Techs, Ivys]
>>> Univs1 = [['MIT', 'Cal Tech'], ['Harvard', 'Yale', 'Brown']]
>>> Univs
[['MIT', 'Cal Tech'], ['Harvard', 'Yale', 'Brown']]
>>> Univs1
[['MIT', 'Cal Tech'], ['Harvard', 'Yale', 'Brown']]
>>> Techs.append('RPI')
>>> Univs
[['MIT', 'Cal Tech', 'RPI'], ['Harvard', 'Yale', 'Brown']]
>>> Techs
['MIT', 'Cal Tech', 'RPI']
>>> Univs1
[['MIT', 'Cal Tech'], ['Harvard', 'Yale', 'Brown']]
>>>
>>>
>>> Techs
['MIT', 'Cal Tech', 'RPI']
>>> Techs[2] = 'WPI'
>>> Techs
['MIT', 'Cal Tech', 'WPI']
>>> Univs
[['MIT', 'Cal Tech', 'WPI'], ['Harvard', 'Yale', 'Brown']]
>>>
>>>
>>> temp = ('one', 'two')
>>> temp
('one', 'two')
>>> temp[1]
'two'
>>> temp[1] = 'three'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
```

--------------------------------------------------------------------------------

Operations on lists
-------------------

##### `Universities.py`

```python
# universities

Techs = ['MIT', 'Cal Tech']
Ivys = ['Harvard', 'Yale', 'Brown']

Univs = [Techs, Ivys]
Univs1 = [['MIT', 'Cal Tech'], ['Harvard', 'Yale', 'Brown']]

Techs.append('RPI')

print('Univs = ')
print(Univs)
print('')
print('Univs1 =')
print(Univs1)


for e in Univs:
    print('Univs contains ')
    print(e)
    print('   which contains')
    for u in e:
        print('      ' + u)
```

```python
>>>
>>> execfile('Universities.py')
Univs =
[['MIT', 'Cal Tech', 'RPI'], ['Harvard', 'Yale', 'Brown']]

Univs1 =
[['MIT', 'Cal Tech'], ['Harvard', 'Yale', 'Brown']]
Univs contains
['MIT', 'Cal Tech', 'RPI']
   which contains
      MIT
      Cal Tech
      RPI
Univs contains
['Harvard', 'Yale', 'Brown']
   which contains
      Harvard
      Yale
      Brown
>>>
>>>
>>> Techs
['MIT', 'Cal Tech', 'RPI']
>>> Techs.append(Ivys)
>>> Techs
['MIT', 'Cal Tech', 'RPI', ['Harvard', 'Yale', 'Brown']]
```

Append versus flatten
---------------------

```python
>>>
>>> execfile('Universities.py')
Univs =
[['MIT', 'Cal Tech', 'RPI'], ['Harvard', 'Yale', 'Brown']]

Univs1 =
[['MIT', 'Cal Tech'], ['Harvard', 'Yale', 'Brown']]
Univs contains
['MIT', 'Cal Tech', 'RPI']
   which contains
      MIT
      Cal Tech
      RPI
Univs contains
['Harvard', 'Yale', 'Brown']
   which contains
      Harvard
      Yale
      Brown
>>> flat = Techs + Ivys
>>> flat
['MIT', 'Cal Tech', 'RPI', 'Harvard', 'Yale', 'Brown']
>>> Techs
['MIT', 'Cal Tech', 'RPI']
>>> Ivys
['Harvard', 'Yale', 'Brown']
```

Cloning
-------

##### `removeDups.py`

```python
def removeDups(L1, L2):
    for e1 in L1:
        if e1 in L2:
            L1.remove(e1)


L1 = [1, 2, 3, 4]
L2 = [1, 2, 5, 6]
removeDups(L1, L2)
print(L1)


def removeDupsBetter(L1, L2):
    L1Start = L1[:]
    for e1 in L1Start:
        if e1 in L2:
            L1.remove(e1)

L1 = [1, 2, 3, 4]
L2 = [1, 2, 5, 6]
removeDupsBetter(L1, L2)
print(L1)
```

```python
>>>
>>> execfile('removeDups.py')
[2, 3, 4]
[3, 4]
```

--------------------------------------------------------------------------------

Functions as Objects
--------------------

##### `applyToEach.py`

```python
# applyToEach


def applyToEach(L, f):
    """assumes L is a list, f a function
       mutates L by replacing each element, e, of L by f(e)"""
    for i in range(len(L)):
        L[i] = f(L[i])


L = [1, -2, 3.4]


def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)


def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

# applyToEach(L, abs)
# print(L)

# applyToEach(L, int)
# print(L)

# applyToEach(L, fact)
# print(L)

# applyToEach(L, fib)
# print(L)


def applyFuns(L, x):
    for f in L:
        print(f(x))
```

Lists of functions
------------------

```python
>>>
>>> execfile('applyToEach.py')
>>> applyFuns([abs, int, fact, fib], 4)
4
4
24
5
```

--------------------------------------------------------------------------------

Dictionaries
------------

```python
>>> monthNumbers = {1: 'Jan', 2: 'Feb', 'Mar': 3, 'Feb': 2, 'Apr': 4, 'Jan': 1, 3: 'Mar'}
>>> monthNumbers
{1: 'Jan', 2: 'Feb', 'Mar': 3, 'Feb': 2, 'Apr': 4, 'Jan': 1, 3: 'Mar'}
>>> monthNumbers['Jan']
1
>>> monthNumbers[2]
'Feb'
>>>
>>>
>>> monthNumbers[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 0
>>> monthNumbers['Apr'] = 4
>>> monthNumbers['Apr']
4
>>>
>>>
>>> collect = []
>>> for e in monthNumbers:
...     collect.append(e)
...
>>> collect
[1, 2, 'Mar', 'Feb', 'Apr', 'Jan', 3]
>>> monthNumbers.keys()
[1, 2, 'Mar', 'Feb', 'Apr', 'Jan', 3]
```

--------------------------------------------------------------------------------

