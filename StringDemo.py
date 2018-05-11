first_name = input("Enter first name : ")
last_name = input("Enter last name : ")
company = input("Enter Company name : ")
address = input("Enter Address : ")

full_name = first_name + " " + last_name

# print("Name is",full_name)

# print("Welcome ",full_name,"to the ICICI")
print("Welcome {} to the ICICI".format(full_name))
# print("Company : {} \nAddress : {}".format(company, address))

print("Company : %s \nAddress : %s"%(company, address))