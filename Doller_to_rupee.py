amount = float(input("Enter the Amount: "))

convert_machine = input(
    "Do you want to convert? (yes/no): "
).lower()

money = input(
    "Enter Dollar or Rupee: "
).lower()

if convert_machine == "yes" or convert_machine == "y":

    if money == "dollar":
        amount = amount / 96
        print(f"Rupee amount in dollars is {round(amount,2)}")

    elif money == "rupee":
        amount = amount * 96
        print(f"dollar amount in Rupees is {round(amount,2)}")

    else:
        print("Invalid currency")

else:
    print("Conversion cancelled")

print("Task Completed")