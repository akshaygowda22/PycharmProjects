import random

target = random.randint(1, 100)

while True:
    user_input = input("Guess the target or Quit (Q): ")

    if user_input.upper() == "Q":
        break

    # Check if user input is a number
    try:
        user_choice = int(user_input)
    except ValueError:
        print("Please enter a valid number or Q to quit.")
        continue

    if user_choice == target:
        print("Success: Correct Guess!!")
        break
    elif user_choice < target:
        print("Your number was too small. Take a bigger guess...")
    else:
        print("Your number was too big. Take a smaller guess...")

print("----GAME OVER----")
