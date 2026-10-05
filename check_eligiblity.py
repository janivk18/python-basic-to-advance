def login():
    employee = input("Show Employee ID: ").lower()
    walkin_code = input("Please enter your walkin code: ").lower()

    if employee == "emp":
        print("Login successful")
        return

    elif walkin_code == "abwc":
        print("Login successful")
        return

    else:
        print("No access to login")


login()

print("This runs after the login function")