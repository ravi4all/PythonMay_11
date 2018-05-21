# lambda expression - anonymous function
# functions without any name
# immediately called and destroyed
# we cannot reuse that function

# def temp_conv(cel):
#     return  9 / 5 * cel + 32

# temp_conv = lambda cel : 9 / 5 * cel + 32
# print(temp_conv(34.5))

temp = [33.5,34.6,32.4,38.7,31.9]

f = list(map(lambda cel : 9 / 5 * cel + 32, temp))
print(f)

even = list(filter(lambda num : num % 2 == 0, [i for i in range(100)]))
print(even)