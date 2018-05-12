Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print(2*1)
2
>>> print(2*2)
4
>>> print(2*3)
6
>>> import turtle
>>> t = turtle.Pen()
>>> t.shape('turtle')
>>> t.forward(100)
>>> t.up()
>>> t.up(90)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    t.up(90)
TypeError: penup() takes 1 positional argument but 2 were given
>>> t.forward(100)
>>> t.reset()
>>> t.forward(100)
>>> turtle.up(90)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    turtle.up(90)
TypeError: up() takes 0 positional arguments but 1 was given
>>> t.reset()
>>> t.forward(100)
>>> t.left(90)
>>> t.forward(100)
>>> t.left(90)
>>> t.forward(100)
>>> t.left(90)
>>> t.forward(100)
>>> t.left(45)
>>> t.forward(100)
>>> t.reset()
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/May_2018/Python_1/Loops/BasicForLoop.py 
Table of 2
2
End of table
4
End of table
6
End of table
8
End of table
10
End of table
12
End of table
14
End of table
16
End of table
18
End of table
20
End of table
Bye
>>> import turtle
>>> t = turtle.Pen()
>>> t.forward(200)
>>> t.left(90)
>>> t.forward(200)
>>> t.left(90)
>>> t.forward(200)
>>> t.left(90)
>>> t.forward(200)
>>> t.left(90)
>>> t.reset()
>>> t.shape('turtle')
>>> t.reset
<bound method RawTurtle.reset of <turtle.Turtle object at 0x000001B301729B00>>
>>> print
<built-in function print>
>>> for i in range(4):
	t.forward(200)
	t.left(90)

	
>>> t.reset()
>>> for i in range(20):
	t.forward(5*i)
	t.left(45)

	
>>> t.reset()
>>> for i in range(50):
	t.forward(2*i)
	t.left(45)

	
>>> t.reset()
>>> for i in range(10):
	t.circle(30)
	t.left(45)

	
>>> t.reset()
>>> for i in range(15):
	t.circle(30)
	t.left(45)

	
>>> t.reset()
>>> for i in range(15):
	t.circle(30)
	t.left(45*i)

	
>>> t.reset()
>>> for i in range(15):
	t.circle(3*i)
	t.left(45)

	
>>> t.reset()
>>> for i in range(15):
	t.circle(10*i)
	t.left(45)

	
>>> t.reset()
>>> t.speed(1)
>>> for i in range(15):
	t.circle(10*i)
	t.left(45)

	
Traceback (most recent call last):
  File "<pyshell#70>", line 3, in <module>
    t.left(45)
  File "C:\Python36\lib\turtle.py", line 1699, in left
    self._rotate(angle)
  File "C:\Python36\lib\turtle.py", line 3276, in _rotate
    self._update()
  File "C:\Python36\lib\turtle.py", line 2663, in _update
    screen._delay(screen._delayvalue) # TurtleScreenBase
  File "C:\Python36\lib\turtle.py", line 566, in _delay
    self.cv.after(delay)
  File "C:\Python36\lib\tkinter\__init__.py", line 741, in after
    self.tk.call('after', ms)
KeyboardInterrupt
>>> t.reset()
]
>>> t.speed(0)
>>> for i in range(50):
	t.circle(5*i)
	t.left(45)

	
>>> t.reset()
>>> t.speed(0)
>>> t.color('red')
>>> for i in range(50):
	t.circle(5*i)
	t.left(45)

	
>>> turtle.Pen()
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    turtle.Pen()
  File "C:\Python36\lib\turtle.py", line 3816, in __init__
    visible=visible)
  File "C:\Python36\lib\turtle.py", line 2557, in __init__
    self._update()
  File "C:\Python36\lib\turtle.py", line 2660, in _update
    self._update_data()
  File "C:\Python36\lib\turtle.py", line 2646, in _update_data
    self.screen._incrementudc()
  File "C:\Python36\lib\turtle.py", line 1292, in _incrementudc
    raise Terminator
turtle.Terminator
>>> t1 = turtle.Pen()
>>> t1.shape('turtle')
>>> colors = ['red','blue','yellow']
>>> import random
>>> for i in range(10):
	t1.color(random.choice(colors))
	t1.circle(i*3)
	t1.left(10)

	
>>> t1.reset()
>>> colors
['red', 'blue', 'yellow']
>>> random.choice(colors)
'yellow'
>>> random.choice(colors)
'red'
>>> random.choice(colors)
'red'
>>> random.choice(colors)
'yellow'
>>> t1.speed(0)
>>> for i in range(50):
	t1.color(random.choice(colors))
	t1.circle(i*3)
	t1.left(10)

	
>>> 
