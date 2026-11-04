# x = {1,2,3,4,5,1,2,3,4,5}
# y = {6,7,8,9,10}
# print(x)
# en_dict = {}
# emp_dict = set()

# print("empty set",emp_dict)

# 1 = [1,22,3]
# print(1.append(55))


# num = int(input("Enter a number: "))

# for i in range(1, 11):
#     print(num, "x", i, "=", num * i)



# Number guessing game .

import random

print("Welcome to Number Guessing Game!")
print("Maine 1 se 100 ke beech ek number socha hai.")
print("Tumhare paas 7 chances hain.")

secret_number = random.randint(1, 100)
chances = 7

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