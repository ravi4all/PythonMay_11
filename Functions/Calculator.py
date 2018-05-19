def add(x,y):
    z = x + y
    print("Addition is",z)

def sub(x,y):
    z = x - y
    print("Subtraction is",z)

def div(x,y):
    z = x / y
    print("Division is",z)

def mul(x,y):
    z = x * y
    print("Multiplication is",z)

# Menu Driven Programs
print("""
1. Add
2. Sub
3. Div
4. Mul
""")

user_choice = input("Enter your choice : ")
num_1 = int(input("Enter first number : "))
num_2 = int(input("Enter second number " ))

todo = {
    "1" : add,
    "2" : sub,
    "3" : div,
    "4" : mul
}

func = todo.get(user_choice)
# print(func)
func(num_1, num_2)