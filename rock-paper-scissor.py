import random

choices = {"r": "rock", "p": "paper", "s": "scissors"}

def get_computer_choice():
    return random.choice(list(choices.keys()))

def get_user_choice():
    print("\nChoose: r for rock, p for paper, s for scissors, e for exit")
    user_choice = input("Enter your choice: ").lower()
    while user_choice not in choices and user_choice != 'e':
        print("Invalid choice.")
        user_choice = input("Enter again (r, p, s, e): ").lower()
    return user_choice

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "r" and computer_choice == "s") or \
         (user_choice == "p" and computer_choice == "r") or \
         (user_choice == "s" and computer_choice == "p"):
        return "You win!"
    else:
        return "Computer wins!"

def display_welcome_message():
    print("\nWelcome to the Rock, Paper, Scissors Game!")
    print("""
      _______               _______
     |       |             |       |
     |   R   |             |   P   |
     |_______|             |_______|
  _______  _______      _______  _______
 |       ||       |    |       ||       |
 |   S   ||   R   |    |   P   ||   S   |
 |_______||_______|    |_______||_______|
 """)

def display_score(user_score, computer_score):
    print("\n-------------------------")
    print(f"Score - You: {user_score} | Computer: {computer_score}")
    print("-------------------------")

user_score = 0
computer_score = 0

display_welcome_message()

while True:
    user_choice = get_user_choice()
    if user_choice == 'e':
        break
    computer_choice = get_computer_choice()
    print(f"\n-------------------------")
    print(f"You chose: {choices[user_choice]}")
    print(f"Computer chose: {choices[computer_choice]}")
    result = determine_winner(user_choice, computer_choice)
    print(result)
    print("-------------------------")
    
    if result == "You win!":
        user_score += 1
    elif result == "Computer wins!":
        computer_score += 1

    display_score(user_score, computer_score)

print("\nThanks for playing! Goodbye!")
