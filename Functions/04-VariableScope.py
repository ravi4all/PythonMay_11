# Scope of variables
# Scope = Local and Global

# global variable
x = 10
y = 12

def add():
    # local variable
    x = 19
    y = 12
    z = x + y
    print("Result is",z)

add()

z = x + y
print("Addition is",z)