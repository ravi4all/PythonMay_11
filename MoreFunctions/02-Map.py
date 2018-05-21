# Map
def temp_conv(cel):
    return  9 / 5 * cel + 32

temp = [33.5,34.6,32.4,38.7,31.9]

# for t in temp:
#     print(temp_conv(t))

f = list(map(temp_conv, temp))
print(f)