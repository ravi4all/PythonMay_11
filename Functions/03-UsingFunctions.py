# x = 10
# y = 12
def add(x,y):    # arguments/parameters
    z = x + y
    print("Addition is",z)

def sub(x,y):
    z = x - y
    print("Subtraction is",z)

def div(x,y):
    z = x / y
    print("Division is",z)

# Default Arguments
def mul(x=10,y=5):
    z = x * y
    print("Multiplication is",z)

add(10,12)
sub(x = 10, y = 12)
div(y = 11, x = 10)
mul(5,6)