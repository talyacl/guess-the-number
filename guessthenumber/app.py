import random

def guess_the_number():
    print("Welcome to Guess the Number!")
    print("I'm thinking of a number between 1 and 100. Can you guess it?")


    secret_number = random.randint(1, 100)
    attempts = 0
    
    while True:
        guess = input("Enter your guess (or 'exit' to quit): ")


        if guess.lower() == 'exit':
            print("Thanks for playing. The number was", secret_number)
            break

        if not guess.isdigit():
            print("Please enter a valid number.")
            continue
        
        guess = int(guess)
        attempts += 1


        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed the number in", attempts, "attempts!")
            break


guess_the_number()