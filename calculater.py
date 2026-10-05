try_again = input("Would you like to try again (yes/no)? ").lower()

while try_again == "yes" or try_again == "y":

    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))

    operation = input("Enter an operation (+, -, /, *, %): ")

    if operation == "+":
        print(num1 + num2)

    elif operation == "-":
        print(num1 - num2)

    elif operation == "/":
        print(num1 / num2)

    elif operation == "%":
        print(num1 % num2)

    elif operation == "*":
        print(num1 * num2)

    else:
        print("Invalid operation")

    # Ask again AFTER calculation
    try_again = input("Would you like to try again (yes/no)? ").lower()

print("Program ended.")