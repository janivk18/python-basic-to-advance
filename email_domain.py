email = input("Enter your email address: ")
domain = email[email.find("@") + 1:]
username = email[:email.find("@")]
print(f"username is {username}")
print(f"domain is {domain}")