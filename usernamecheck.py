username = input("Enter a username: ")
if len(username) > 12:
    print("username too long and can't more then 12 charecters")
elif not username.find(" ") == -1:
    print("username can't have space")
elif not username.isalpha():
    print("username can't have digits")
else:
    print(username,"Welcome")