import random

print("Welcome to Number Guessing Game!")
print("Maine 1 se 50 ke beech ek number socha hai.")
print("Tumhare paas 5 chances hain.")

secret_number = random.randint(1, 50)
chances = 5

for attempt in range(1, chances + 1):
    guess = int(input(f"\nAttempt {attempt}: Apna guess likho: "))

    if guess == secret_number:
        print("Shabash! Dhiraj Sahi guess!")
        print(f"Tumne {attempt} attempt mein jeeta.")
        break
    elif guess < secret_number:
        print("Thoda bada number socho.")
    else:
        print("Thoda chhota number socho.")

else:
    print("\nGame over! Sahi number tha:", secret_number)