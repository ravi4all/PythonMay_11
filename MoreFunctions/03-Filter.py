def even_num(num):
    return num % 2 == 0

# num = 10
numbers = [2,4,7,8,11,15,19,21,32]
# print(even_num(10))

# even = []
#
# for n in numbers:
#     # print(even_num(n))
#     if even_num(n):
#         even.append(n)
#
# print(even)

even = list(filter(even_num, numbers))
print(even)