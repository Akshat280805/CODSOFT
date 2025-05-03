import random

def get_user_choice():
    print("\nWhat do you pick? (rock / paper / scissors)")
    choice = input("Your choice: ").strip().lower()
    return choice

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(player, computer):
    if player == computer:
        return "tie"
    elif (
        (player == 'rock' and computer == 'scissors') or
        (player == 'scissors' and computer == 'paper') or
        (player == 'paper' and computer == 'rock')
    ):
        return "user"
    else:
        return "computer"

def play_round():
    user_choice = get_user_choice()
    while user_choice not in ['rock', 'paper', 'scissors']:
        print("Oops! That's not a valid choice. Try again.")
        user_choice = get_user_choice()

    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)

    if result == "tie":
        print("It's a tie! Nobody wins this one.")
    elif result == "user":
        print("You win! 🎉")
    else:
        print("Computer wins this round. 😐")

    return result

def rock_paper_scissors():
    print("=== Welcome to Rock-Paper-Scissors! ===")
    print("First to 3 wins! (or press Ctrl+C anytime to quit)\n")

    user_score = 0
    computer_score = 0

    while True:
        outcome = play_round()

        if outcome == "user":
            user_score += 1
        elif outcome == "computer":
            computer_score += 1

        print(f"Score => You: {user_score} | Computer: {computer_score}")

        if user_score == 3:
            print("\n🏆 Congratulations! You beat the computer.")
            break
        elif computer_score == 3:
            print("\n💻 The computer wins the match. Better luck next time!")
            break

        cont = input("\nPlay another round? (yes to continue): ").strip().lower()
        if cont != 'yes':
            print("Thanks for playing! 👋")
            break

if __name__ == "__main__":
    rock_paper_scissors()
