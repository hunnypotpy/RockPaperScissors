import random

user_answer = input("Enter a choice (rock(1), paper(2), scissors(3)): ")
possible_actions = ['1','2','3']
computer_answer = random.choice(possible_actions)
print(f"\nYou chose {user_answer}, computer chose {computer_answer}.\n")

if user_answer == computer_answer:
    print(f"Both players selected {user_answer}. It's a tie!")
elif user_answer == '1':
    if computer_answer == '3':
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif user_answer == '2':
    if computer_answer == '1':
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif user_answer == '3':
    if computer_answer == '2':
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")

            