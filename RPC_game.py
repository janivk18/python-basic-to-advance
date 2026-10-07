import random

options = ["rock", "paper", "scissors"]

while True:
    result = random.choice(options)

    user_input = input("Enter an option (rock/paper/scissors, q to quit): ").lower()

    if user_input == "q" or user_input == "quit":
        break

    if user_input not in options:
        print("Invalid option!")
    elif user_input == result:
        print("Correct!")
    else:
        print(f"Wrong! Computer chose {result}")

print(f"--- GAME OVER ---")