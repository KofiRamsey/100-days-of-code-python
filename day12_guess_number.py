import random
from day12_guess_number_art import logo

print(logo)

number_to_guess = random.randint(1, 100)
print("I'm thinking of a number between 1 and 100.")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == 'easy':
    attempts = 10
elif difficulty == 'hard':
    attempts = 5

game_over = False
while not game_over and attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))

    if guess > number_to_guess:
        print("Too high.")
        attempts -= 1
    elif guess < number_to_guess:
        print("Too low.")
        attempts -= 1
    else:
        game_over = True
        print(f"You got it! The answer was {number_to_guess}.")

if attempts == 0:
    print(f"You've run out of guesses, you lose. The answer was {number_to_guess}.")
