students= []
student_data = {}

while True:
    name = input("Enter your name : ")
    age = int(input("Enter your age : "))
    address = input("Enter your address : ")

    student_data['name'] = name
    student_data['age'] = age
    student_data['address'] = address

    print("Data Inserted Successfully...")
    students.append(student_data.copy())
    for data in students:
        print(data)
