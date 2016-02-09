Scalar objects
--------------

```python
>>> 3
3
>>> true
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'true' is not defined
>>> True
True
>>> type(3)
<type 'int'>
>>> type(3.0)
```

Operators on `ints` and `floats`
--------------------------------

```python
>>> 3 + 4
7
>>> 3.0 + 4
7.0
>>> 3-4
-1
>>> 3 * 4
12
>>>
>>>
>>>
>>> 3.0/2.0
1.5
>>> 3.0/2
1.5
>>> 3/2
1
>>> 3%2
1
>>> 3**2
9
>>>
>>>
>>>
>>> (2+3)*4
20
>>> 2+3*4
14
```

Comparison operators on `ints` and `floats`
-------------------------------------------

```python
>>> 3 > 4
False
>>> 3 > 3
False
>>> 3 >= 3
True
>>> 3 == 3
True
>>> 3 != 3
False
>>> 3 != 4
True
```

Type conversions (type casting)
-------------------------------

```python
>>> float(3)
3.0
>>> int(3.0)
3
>>> int(3.9)
3
```

--------------------------------------------------------------------------------

Binding variables and values
----------------------------

```python
>>> pi = 3.14159
>>> pi
3.14159
>>> radius = 11.2
>>> radius
11.2
>>> area = pi * (radius ** 2)
>>> area
394.0810495999999
```

Changing bindings
-----------------

```
>>> radius
11.2
>>> radius = 14.3
>>> radius
14.3
>>> area
394.0810495999999
>>>
```

--------------------------------------------------------------------------------

Non-scalar objects
------------------

```python
>>> 'abc'
'abc'
>>> foo = 'abc'
>>> foo
'abc'
>>> type(foo)
<type 'str'>
>>>
>>>
>>>
>>> '123'
'123'
>>> type('123')
<type 'str'>
>>> type(123)
<type 'int'>
>>>
```

Operators on strings
--------------------

```python
>>> 3 * 'a'
'aaa'
>>> 3 * 'ab'
'ababab'
>>> 'a' + 'b'
'ab'
>>> 'a' + str(123)
'a123'
>>> len('abc')
3
```

Extracting parts of strings
---------------------------

```
>>> 'abc'[1]
'b'
>>> 'abc'[1:3]
'bc'
```

--------------------------------------------------------------------------------

Programs (or scripts)
---------------------

```python
>>> print('abc')
abc
>>> print(3 * 'a')
aaa
```

Providing input
---------------

```python
>>> name = raw_input('Enter your name: ')
Enter your name: Eric Grimson
>>> name
'Eric Grimson'
>>> print('Are you ' + name + '?')
Are you 'Eric Grimson'?
>>>
```

Straight line program
---------------------

##### `lec2.5.4.py`

```python
## Lec 2.5, slide 4

x = 3
x = x*x #square value of x
print(x)
y = float(raw_input('Enter a number: '))
print(y*y)
```

```python
>>> execfile('lec2.5.4.py')
9
Enter a number: 4
16.0
```

--------------------------------------------------------------------------------

Branching programs
------------------

##### `lec2.6.2.py`

```python
# Lec 2.6, slide 2

x = int(raw_input('Enter an integer: '))
if x%2 == 0:
    print('')
    print('Even')
else:
    print('')
    print('Odd')
print('Done with conditional')
```

```python
>>> execfile('lec2.6.2.py')
Enter an integer: 5

Odd
Done with conditional
>>>
```

##### `lec2.6.4.py`

```python
# Lec 2.6, slide 4

x = 6

if x%2 == 0:
    if x%3 == 0:
        print('Divisible by 2 and 3')
    else:
        print('Divisible by 2 and not by 3')
elif x%3 == 0:
    print('Divisible by 3 and not by 2')
```

```python
>>> execfile('lec2.6.4.py')
Divisible by 2 and 3
```

##### `lec2.6.4.py` modified 1

```python
# Lec 2.6, slide 4

x = 5

if x%2 == 0:
    if x%3 == 0:
        print('Divisible by 2 and 3')
    else:
        print('Divisible by 2 and not by 3')
elif x%3 == 0:
    print('Divisible by 3 and not by 2')
```

```
>>> execfile('lec2.6.4.py')
>>>
```

##### `lec2.6.4.py` modified 2

```python
# Lec 2.6, slide 4

x = 5

if x%2 == 0:
    if x%3 == 0:
        print('Divisible by 2 and 3')
    else:
        print('Divisible by 2 and not by 3')
elif x%3 == 0:
    print('Divisible by 3 and not by 2')
else:
    print('Not divisible by 2 or 3')
```

```
>>> execfile('lec2.6.4.py')
Not divisible by 2 or 3
```

