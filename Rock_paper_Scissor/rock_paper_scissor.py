import random


def play():
    user = input(
        "What is your choice? 'r' for rock, 'p' for paper, 's' for scissor  ")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return "It's a tie"
    if is_win(user, computer):
        return "Player Win"
    return "You lost"


def is_win(player, opponent):
    # return true if player win
    # r>s, s>p, p>r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True


p = play()
print(p)
