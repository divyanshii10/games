import random

def user_turn():
    while True:
        try:
            user_pick = int(input("Enter the number of balls you want to pick (1-4): "))
            if 1 <= user_pick <= 4:
                return user_pick
            else:
                print("Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def computer_turn(remaining_balls):
    # Ensure the computer always wins by picking a number that leaves a multiple of 5
    return (remaining_balls - 1) % 5

def play_game():
    total_balls = 51
    current_turn = "user"

    print("Welcome to the game of picking balls!")
    print("You are playing against the computer.")

    while total_balls > 0:
        if current_turn == "user":
            print("\nCurrent number of balls in the basket:", total_balls)
            user_pick = user_turn()
            total_balls -= user_pick
            print("You picked", user_pick, "ball(s).")
            current_turn = "computer"
        else:
            computer_pick = computer_turn(total_balls)
            total_balls -= computer_pick
            print("Computer picked", computer_pick, "ball(s).")
            current_turn = "user"

    if current_turn == "user":
        print("\nSorry, you lose! The computer picked the last ball.")
    else:
        print("\nCongratulations! You picked the last ball. You win!")

play_game()

