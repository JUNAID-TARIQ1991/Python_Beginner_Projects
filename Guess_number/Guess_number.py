import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Enter a number between 1 anf {x}: "))
        if guess > random_number:
            print("Your Guess is too high")
        elif guess < random_number:
            print("Your Guess is too low")
    print("Wow! you guess right")


def main():
    guess(10)


main()
