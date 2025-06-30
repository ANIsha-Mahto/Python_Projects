import random

def play_game():
    print("Welcome to the Number Guessing Game!!")
    print("I'm thinking of a number between 1 and 100.")

    difficulty = input("Choose a difficulty (easy / medium / hard): ").lower()
    if difficulty == "easy":
        max_attempts = 15
    elif difficulty == "medium":
        max_attempts = 10
    elif difficulty == "hard":
        max_attempts = 5
    else:
        print("Invalid choice! Defaulting to medium.")
        max_attempts = 10

    number_to_guess = random.randint(1, 100)
    attempts = 0
    won = False

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts} - Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1
        if guess < number_to_guess:
            print("Too low! Try again 🥺")
        elif guess > number_to_guess:
            print("Too high! Try again 🥺")
        else:
            print(f"🎉 Congratulations! You guessed the number in {attempts} tries.")
            won = True
            break

    if not won:
        print(f"😢 You've run out of attempts! The number was {number_to_guess}.")

    return won

games_played = 0
games_won = 0

while True:
    if play_game():
        games_won += 1
    games_played += 1

    print(f"\n📊 Scoreboard — Games Played: {games_played}, Games Won: {games_won}")
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again != 'yes':
        print("Thanks for playing! 👋")
        break
