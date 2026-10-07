# ==========================================
# ADVANCED FOOD ORDERING / SHOPPING CART
# ==========================================

cart = []

TAX_RATE = 0.05
DELIVERY_CHARGE = 40
FREE_DELIVERY_LIMIT = 500


# ------------------------------------------
# INPUT VALIDATION
# ------------------------------------------

def get_positive_float(message):
    while True:
        try:
            value = float(input(message))
            if value <= 0:
                print("Please enter a value greater than 0.")
            else:
                return value
        except ValueError:
            print("Please enter a valid number.")


def get_positive_int(message):
    while True:
        try:
            value = int(input(message))
            if value <= 0:
                print("Please enter a quantity greater than 0.")
            else:
                return value
        except ValueError:
            print("Please enter a valid whole number.")


# ------------------------------------------
# ADD ITEM
# ------------------------------------------

def add_item():
    food = input("Enter food name: ").strip().lower()

    if not food:
        print("Food name cannot be empty.")
        return

    price = get_positive_float(f"Enter price of {food} $: ")
    quantity = get_positive_int("Enter quantity: ")

    # Check if item already exists
    for item in cart:
        if item["food"] == food:
            item["quantity"] += quantity
            print(f"{food} quantity updated successfully.")
            return

    # Add new item
    cart.append({
        "food": food,
        "price": price,
        "quantity": quantity
    })

    print(f"{quantity} x {food} added to cart.")


# ------------------------------------------
# VIEW CART
# ------------------------------------------

def view_cart():
    if not cart:
        print("\nYour cart is empty.")
        return

    print("\n" + "=" * 55)
    print("                    YOUR CART")
    print("=" * 55)

    print(f"{'Food':<20}{'Price':<12}{'Qty':<8}{'Total':<12}")
    print("-" * 55)

    subtotal = 0

    for item in cart:
        item_total = item["price"] * item["quantity"]
        subtotal += item_total

        print(
            f"{item['food']:<20}"
            f"${item['price']:<11.2f}"
            f"{item['quantity']:<8}"
            f"${item_total:<11.2f}"
        )

    print("-" * 55)
    print(f"{'Subtotal:':<40} ${subtotal:.2f}")
    print("=" * 55)


# ------------------------------------------
# REMOVE ITEM
# ------------------------------------------

def remove_item():
    if not cart:
        print("\nYour cart is empty.")
        return

    food = input("Enter food to remove: ").strip().lower()

    for item in cart:
        if item["food"] == food:
            cart.remove(item)
            print(f"{food} removed from cart.")
            return

    print("Food not found in cart.")


# ------------------------------------------
# UPDATE QUANTITY
# ------------------------------------------

def update_quantity():
    if not cart:
        print("\nYour cart is empty.")
        return

    food = input("Enter food name: ").strip().lower()

    for item in cart:
        if item["food"] == food:
            quantity = get_positive_int("Enter new quantity: ")
            item["quantity"] = quantity
            print(f"{food} quantity updated.")
            return

    print("Food not found in cart.")


# ------------------------------------------
# CALCULATE SUBTOTAL
# ------------------------------------------

def calculate_subtotal():
    subtotal = 0

    for item in cart:
        subtotal += item["price"] * item["quantity"]

    return subtotal


# ------------------------------------------
# APPLY DISCOUNT
# ------------------------------------------

def calculate_discount(subtotal):
    discount = 0

    if subtotal >= 1000:
        discount = subtotal * 0.15
        print("15% discount applied!")

    elif subtotal >= 500:
        discount = subtotal * 0.10
        print("10% discount applied!")

    elif subtotal >= 300:
        discount = subtotal * 0.05
        print("5% discount applied!")

    return discount


# ------------------------------------------
# CHECKOUT
# ------------------------------------------

def checkout():
    if not cart:
        print("\nYour cart is empty. Add something first.")
        return

    subtotal = calculate_subtotal()
    discount = calculate_discount(subtotal)

    amount_after_discount = subtotal - discount

    tax = amount_after_discount * TAX_RATE

    if amount_after_discount >= FREE_DELIVERY_LIMIT:
        delivery = 0
    else:
        delivery = DELIVERY_CHARGE

    final_total = amount_after_discount + tax + delivery

    print("\n" + "=" * 60)
    print("                    FINAL RECEIPT")
    print("=" * 60)

    print(f"{'Food':<20}{'Qty':<8}{'Amount':<12}")
    print("-" * 60)

    for item in cart:
        amount = item["price"] * item["quantity"]

        print(
            f"{item['food']:<20}"
            f"{item['quantity']:<8}"
            f"${amount:<11.2f}"
        )

    print("-" * 60)

    print(f"{'Subtotal':<45} ${subtotal:.2f}")
    print(f"{'Discount':<45} -${discount:.2f}")
    print(f"{'Tax (5%)':<45} ${tax:.2f}")
    print(f"{'Delivery':<45} ${delivery:.2f}")
    print("-" * 60)
    print(f"{'FINAL TOTAL':<45} ${final_total:.2f}")
    print("=" * 60)

    print("Thank you for your order! 🍔")


# ------------------------------------------
# SEARCH ITEM
# ------------------------------------------

def search_item():
    if not cart:
        print("\nYour cart is empty.")
        return

    search = input("Enter food name to search: ").strip().lower()

    found = False

    for item in cart:
        if search in item["food"]:
            print(
                f"Found: {item['food']} | "
                f"Price: ${item['price']:.2f} | "
                f"Quantity: {item['quantity']}"
            )
            found = True

    if not found:
        print("No matching food found.")


# ==========================================
# MAIN PROGRAM
# ==========================================

while True:

    print("\n" + "=" * 45)
    print("          FOOD ORDERING SYSTEM")
    print("=" * 45)

    print("1. Add food")
    print("2. View cart")
    print("3. Remove food")
    print("4. Update quantity")
    print("5. Search food")
    print("6. Checkout")
    print("7. Exit")

    choice = input("\nChoose an option: ").strip()

    if choice == "1":
        add_item()

    elif choice == "2":
        view_cart()

    elif choice == "3":
        remove_item()

    elif choice == "4":
        update_quantity()

    elif choice == "5":
        search_item()

    elif choice == "6":
        checkout()

        # Clear cart after successful checkout
        cart.clear()
        print("Cart cleared.")

    elif choice == "7":
        print("Thank you! Program ended.")
        break

    else:
        print("Invalid option. Please choose 1-7.")