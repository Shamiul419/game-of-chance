import random

money = 100


def flip_function(guess,bet):
    num = random.randint(1,2)
    if num == 1 and guess == "Heads":
        return "Heads"
    elif num != 1 and guess == "Tails":
        return "Tails"
    else:
        return "You have failed."

print(flip_function("Heads",1))
