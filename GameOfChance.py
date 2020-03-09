import random

money = 100
new_money=0

def flip_function(guess,bet):
    num = random.randint(1,2)
    if num == 1 and guess == "Heads":
        print(money+bet)
        return "Heads"
    elif num != 1 and guess == "Tails":
        print(money+bet)
        return "Tails"

    else:
        print(money-bet)
        return "You have failed."
        
print(flip_function("Heads",2))
