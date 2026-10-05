item = input("What is the item? ")
price = float(input("Enter the price of the item: "))
quantity = float(input("Enter the quantity of the item: "))
total = price * quantity
print(f"Total {item} you ordered is {quantity}")
print(f"Total bill is {round(total,2)}")