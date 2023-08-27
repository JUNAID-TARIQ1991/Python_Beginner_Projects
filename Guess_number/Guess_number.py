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


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:

            guess = random.randint(low, high)
        else:
            guess = low  # it can be high because both are same
        feedback = input(
            f"is guess {guess} is too high (H), too low (L) or correct (c)  ".lower())
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f"Wow! computer guess your number {guess}")


def main():
    computer_guess(100)


main()
