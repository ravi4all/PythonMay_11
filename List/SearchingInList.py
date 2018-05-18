users = []
userdata = {}

while True:
    print("""
    1. Add User
    2. Delete User
    3. Search User
    """)
    user_choice = input("Enter your choice : ")

    if user_choice == "1":
        username = input("Enter your name : ")
        userage = int(input("Enter your age : "))
        usercompany = input("Enter your company : ")

        userdata['name'] = username
        userdata['age'] = userage
        userdata['company'] = usercompany

        users.append(userdata.copy())

    elif user_choice == "2":
        pass

    elif user_choice == "3":
        search = input("Enter the name of user : ")

        for user in users:
            if user['name'] == search:
                print(user)

    else:
        break