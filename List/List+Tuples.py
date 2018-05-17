Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> list_1 = []
>>> list_1.append(12)
>>> list_1
[12]
>>> list_1.append(18)
>>> list_1
[12, 18]
>>> list_1.append(28)
>>> list_1
[12, 18, 28]
>>> list_1.append('hi')
>>> list_1.append('hello')
>>> list_1
[12, 18, 28, 'hi', 'hello']
>>> list_1.append(9,8,7,6,5)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    list_1.append(9,8,7,6,5)
TypeError: append() takes exactly one argument (5 given)
>>> list_1.append(9)
>>> list_1
[12, 18, 28, 'hi', 'hello', 9]
>>> list_1.insert(0,'python')
>>> list_1
['python', 12, 18, 28, 'hi', 'hello', 9]
>>> list_1.pop()
9
>>> list_1.pop()
'hello'
>>> list_1
['python', 12, 18, 28, 'hi']
>>> list_1.pop(2)
18
>>> list_1
['python', 12, 28, 'hi']
>>> list_2 = [100,101,102,103,104]
>>> list_3 = list_1 + list_2
>>> list_3
['python', 12, 28, 'hi', 100, 101, 102, 103, 104]
>>> a = 'hi'
>>> for i in range(len(list_3)):
	if list_3[i] == a:
		list_3.pop(i)

		
'hi'
Traceback (most recent call last):
  File "<pyshell#29>", line 2, in <module>
    if list_3[i] == a:
IndexError: list index out of range
>>> list_3
['python', 12, 28, 100, 101, 102, 103, 104]
>>> b = 'python'
>>> b in list_3
True
>>> list_3.index('python')
0
>>> list_3.remove('python')
>>> list_3
[12, 28, 100, 101, 102, 103, 104]
>>> list_4 = [3,4,6,7,1,2,4,23,45,12,26,17,20]
>>> list_4.sort()
>>> list_4
[1, 2, 3, 4, 4, 6, 7, 12, 17, 20, 23, 26, 45]
>>> list_4.sort(reversed = True)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    list_4.sort(reversed = True)
TypeError: 'reversed' is an invalid keyword argument for this function
>>> list_4.sort(reverse = True)
>>> list_4
[45, 26, 23, 20, 17, 12, 7, 6, 4, 4, 3, 2, 1]
>>> tup_1 = 100,101
>>> tup_1
(100, 101)
>>> tup_1 = (10,12,13,14,15)
>>> tup_1[0]
10
>>> tup[1]
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    tup[1]
NameError: name 'tup' is not defined
>>> tup_2[1]
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    tup_2[1]
NameError: name 'tup_2' is not defined
>>> tup_1[1]
12
>>> list_1[2]
28
>>> list_3[1]
28
>>> list_1[0:]
['python', 12, 28, 'hi']
>>> list_1[-1]
'hi'
>>> list_2[1:4]
[101, 102, 103]
>>> tup_1[1:3]
(12, 13)
>>> list_1
['python', 12, 28, 'hi']
>>> list_1[0] = 'bye'
>>> list_!
SyntaxError: invalid syntax
>>> list_1
['bye', 12, 28, 'hi']
>>> tup_1
(10, 12, 13, 14, 15)
>>> tup_1[0] = 'bye'
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    tup_1[0] = 'bye'
TypeError: 'tuple' object does not support item assignment
>>> 
