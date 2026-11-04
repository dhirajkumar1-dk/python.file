import random

choices = ["rock", "paper", "scissors"]

print("Welcome to Rock, Paper, Scissors!")
print("Rules: rock beats scissors, scissors beats paper, paper beats rock.")
print("Game khatam karne ke liye 'quit' likho.\n")

player_score = 0
computer_score = 0

while True:
    player = input("Apni choice likho (rock / paper / scissors): ").lower()

    if player == "quit":
        print("\nGame khatam!")
        print(f"Tumhara score: {player_score}")
        print(f"Computer ka score: {computer_score}")
        break

    if player not in choices:
        print("Galat choice! Sirf rock, paper ya scissors likho.")
        continue

    computer = random.choice(choices)

    print(f"\nTumne chuna: {player}")
    print(f"Computer ne chuna: {computer}")

    if player == computer:
        print("Result: Tie!")
    elif (
        (player == "rock" and computer == "scissors")
        or (player == "paper" and computer == "rock")
        or (player == "scissors" and computer == "paper")
    ):
        print("Result: Tum jeet gaye!")
        player_score += 1
    else:
        print("Result: Computer jeet gaya!")
        computer_score += 1

    print(f"Score -> Tum {player_score} : Computer {computer_score}\n")