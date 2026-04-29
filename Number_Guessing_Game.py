import random

# Store best (lowest) attempts for each difficulty
best_scores = {
    "easy": None,
    "medium": None,
    "hard": None
}


def choose_difficulty():
    print("\nSelect Difficulty Level:")
    print("1. Easy (1 to 10)")
    print("2. Medium (1 to 50)")
    print("3. Hard (1 to 100)")

    while True:
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            return "easy", 10
        elif choice == "2":
            return "medium", 50
        elif choice == "3":
            return "hard", 100
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")


def play_game():
    difficulty, max_range = choose_difficulty()

    secret_number = random.randint(1, max_range)
    attempts = 0

    print(f"\nI have selected a number between 1 and {max_range}.")
    print("Try to guess it!")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try a higher number.")
            elif guess > secret_number:
                print("Too high! Try a lower number.")
            else:
                print(f"\n🎉 Correct! You guessed the number in {attempts} attempts.")

                # Update best score
                if best_scores[difficulty] is None or attempts < best_scores[difficulty]:
                    best_scores[difficulty] = attempts
                    print("🏆 New Best Score!")
                else:
                    print(f"Best Score for {difficulty.title()}: {best_scores[difficulty]} attempts")

                break

        except ValueError:
            print("Please enter a valid number!")


def main():
    print("===== Number Guessing Game =====")

    while True:
        play_game()

        replay = input("\nDo you want to play again? (yes/no): ").lower()

        if replay != "yes":
            print("\nThanks for playing!")
            print("Final Best Scores:")
            for level, score in best_scores.items():
                if score is not None:
                    print(f"{level.title()}: {score} attempts")
                else:
                    print(f"{level.title()}: No score yet")
            break


# Run the program
main()