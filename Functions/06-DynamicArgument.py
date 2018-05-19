# *args
# **kwargs
def student(id,name,age,*address):
    print("ID : {}".format(id))
    print("Name : {}".format(name))
    print("Age : {}".format(age))
    # print("Address : {}".format(address))
    # for i in range(len(address)):
    #     print("Address {} : {}".format(i+1,address[i]))

    for i, addr in enumerate(address):
        print("Address {} : {}".format(i+1,addr))

# student(101,'Ram',14,'Rohini','Rithala')
# print("")
# student(101,'Ram',14,'Rohini','Rithala','NSP')
# print("")
# student(101,'Ram',14,'Rohini')

# Address 1 : 'Rohini'
# Address 2 : 'Rithala'

def student_details(**details):
    print(details)

student_details(name = 'Ram', age = 13, address = 'Rohini')
student_details(name = 'Shyam', age = 12, hobby = 'Cricket')
student_details(name = 'Rohan', address = 'Rithala', hobby = 'Cricket')