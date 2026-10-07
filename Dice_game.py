import random
low = 1
high = 10
result = random.randint(low, high)

user_input = int(input("Enter a number: "))
if user_input == result:
    print("Correct!")
else:
    print("Incorrect!")