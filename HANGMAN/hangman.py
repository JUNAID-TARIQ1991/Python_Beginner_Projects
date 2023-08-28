import random
import string
from words import words


def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word


def hangman():
    word = get_valid_word(words)
    word_letter = set(word)
    alphabets = set(string.ascii_uppercase)
    used_letter = set()
    lives = 6

    while len(word_letter) > 0 and lives > 0:
        print("You have", lives, " lives left, You have used these letters: ",
              ' '.join(used_letter))

        # Update word_list to display guessed letters
        word_list = [
            letter if letter in used_letter else '-' if letter.isalpha() else letter for letter in word]

        print("Current word:", ' '.join(word_list))

        user_letter = input("Guess a letter: ").upper()

        if user_letter in alphabets - used_letter:
            used_letter.add(user_letter)
            if user_letter in word_letter:
                word_letter.remove(user_letter)
            else:
                lives -= 1
                print("Letter is not in the word")
        elif user_letter in used_letter:
            print("You have already used that character! Please try again")
        else:
            print("You have entered an invalid character! Try again")

    if lives == 0:
        print("You ran out of lives! The word was:", word)
    else:
        print("Congratulations! You guessed the word:", word)


hangman()
