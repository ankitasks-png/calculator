import random

def guess_number():
    number_to_guess = random.randint(1, 100)
    print("Welcome to the Number Guessing Game!")
    print("Guess a number between 1 and 100")

    while True:
        guess = int(input("Enter your guess: "))
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed the number.")
            break

guess_number()

