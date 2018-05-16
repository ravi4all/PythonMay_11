min_range = int(input("Enter minimum range : "))
max_range = int(input("Enter maximum range : "))

# min - 10
# max - 100

for num in range(min_range, max_range):
    for i in range(2,num):
        if num % i == 0:
            print("{} is not a prime number".format(num))
            break
    else:
        print("{} is a prime number".format(num))