from random import randint

def introduction():
    print("Welcome to the Number Guessing Game. \n"
          "I will generate a random number between 1 and 100 that you will have to guess. \n"
          "You can choose between three difficulties: Easy, Medium and Hard. \n"
          "This will affect the amount of guesses you have: \n"
          "Easy - 10 \n"
          "Medium - 5 \n"
          "Hard - 3 \n")

def easy(number):
    guesscount = 0
    while guesscount < 10:
        guess = int(input("What is your guess: "))
        if guess == number:
            print(f"Congratulations! You guessed correctly on guess {guesscount}!")
            print(f"The number was: {number}")
            return
        else:
            if guess > number:
                print("The number is lower than your guess.")
            elif guess < number:
                print("The number is greater than your guess")
            guesscount += 1
            print(f"Attempt {guesscount} of 10.")

    print("You couldn't guess the number correctly.")
    print(f"The number to guess was: {number}")

def medium(number):
    guesscount = 0
    while guesscount < 5:
        guess = int(input("What is your guess: "))
        if guess == number:
            print(f"Congratulations! You guessed correctly on guess {guesscount}!")
            print(f"The number was: {number}")
            return
        else:
            if guess > number:
                print("The number is lower than your guess")
            elif guess < number:
                print("The number is greater than your guess")
            guesscount += 1
            print(f"Attempt {guesscount} of 5.")

    print("You couldn't guess the number correctly.")
    print(f"The number to guess was: {number}")

def hard(number):
    guesscount = 0
    while guesscount < 3:
        guess = int(input("What is your guess: "))
        if guess == number:
            print(f"Congratulations! You guessed correctly on guess {guesscount}!")
            print(f"The number was: {number}")
            return
        else:
            if guess > number:
                print("The number is lower than your guess")
            elif guess < number:
                print("The number is greater than your guess")
            guesscount += 1
            print(f"Attempt {guesscount} of 3.")

    print("You couldn't guess the number correctly.")
    print(f"The number to guess was: {number}")

def main():
    introduction()
    difficulty = input("Which difficulty will you choose? ").lower()
    number = randint(1, 100)

    if difficulty == "easy":
        easy(number)
    elif difficulty == "medium":
        medium(number)
    elif difficulty == "hard":
        hard(number)
    else:
        print("Invalid difficulty selected.")

if __name__ == "__main__":
    main()