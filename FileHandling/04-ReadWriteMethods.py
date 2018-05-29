# bf default open in read mode
file = open('text_2.txt')

# will read till 10 characters from beginning
# data = file.read(10)

# will not read 10 characters from last
# data = file.read(-10)

# will return whole data in a list
# data = file.readlines()

# will read data line by line
data = file.readline()
print(data)

file.close()