def outer():
    print("This is outer function")
    x = 10
    y = 12

    def inner_1():
        z = x + y
        print("This is inner_1 function",z)

    def inner_2():
        z = x - y
        print("This is inner_2 function",z)

    def inner_3():
        z = x * y
        print("This is inner_3 function",z)

    # inner_1()
    # inner_2()
    # inner_3()
    return inner_2

func_1 = outer()
func_1()