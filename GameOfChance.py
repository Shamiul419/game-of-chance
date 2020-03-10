import random

money = 100

def flip_function(guess,bet):
    num=random.randint(1,2)
    print("-----------------------------")
    print("Lets play a coin flip game.")
    print("-----------------------------")

#Checks if your bet is greater than 0.
    if bet <= 0:
        print("Your bet should be greater than 0.")
        return 0
#Gets Heads or Tails.
    if num == 1:
        print("Heads!")
    elif num == 2:
        print("Tails!")

    print("You have chosen, " + str(guess) )
#Starts the game.
    if guess == "Heads" and num == 1:
        print("You have won!!!")
        print("You have won " + str(bet)+ " amount of dollars")
        return +bet
    elif guess == "Tails" and num == 2:
        print("You have won!!!")
        print("You have won " + str(bet) + " amount of dollars")
        return +bet
    else:
        print("You have lost the bet.")
        print("You have lost " + str(bet) + " amount of money")
        return -bet

def card_game(bet):
    print("-----------------------------")
    print("Let's play a card game.")
    print("-----------------------------")

#Checks if your bet is greater than 0.
    if bet <= 0:
        print("Your bet should be greater than 0.")
        return 0
#Genarates a number.
    my_cards =random.randint(1,10)
    their_cards =random.randint(1,10)
#Starts the card count.
    print("Your card was " + str(my_cards))
    print("AI card was " + str(their_cards))
#Starts the game.
    if my_cards > their_cards:
        print("You have won!!!")
        print("You have won " + str(bet) +" amount of dollars!")
        return +bet
    elif my_cards < their_cards:
        print("You have lost!!!")
        print("You have lost " + str(bet) +" amount of dollars!")
        return -bet
    elif my_cards==their_cards:
        print("It's a tie.")
        return 0


def cho_han(guess,bet):
    print("-----------------------------")
    print("Let's play a dice game.")
    print("-----------------------------")
#Checks if your bet is greater than 0.
    if bet <= 0:
        print("Your bet should be greater than 0.")
        return 0
    pirnt("You have chosen " + str(guess) +" and " + str(bet) +" amount of dollars.")
#Genarates the number.
    first_dice = random.randint(1,6)
    second_dice = random.randint(1,6)
    total_number=dice1 + dice2
#Starts the game.
    if total % 2 ==0 and guess == "Even":
        print("You have won!!")
        return +bet
    elif total % 2 !=0 and guess == "Odd":
        print("You have won!!")
        return +bet
    else:
        print("You have lost")
        return -bet

def roulette(guess,bet):
    print("-----------------------------")
    print("Let's play a roulette game.")
    print("-----------------------------")
#Checks if your bet is greater than 0.
    if bet <= 0:
        print("Your bet should be greater than 0.")
        return 0
#Genarates the number.
    number = random.randint(1,37)
#Some rules.
    if number == 37:
        print("The wheel landed on 00")
    else:
        print("The wheel landed on " + str(guess))
#More rules.
    if guess == "Even" and number % 2 ==0 and number != 0:
        print(str(number) + " is a Even number.")
        print("You have won " + str(bet) + " amount of dollars!!!")
        return bet
    elif guess == "Odd" and number % 2 ==1 and number != 37:
        print(str(number) + " is a Odd number.")
        print("You have won " + str(bet) + " amount of dollars!!!")
        return bet
#Starts the game.
    elif guess == bet:
        print("You have guessed " + str(guess) + " and the result was " +str(number))
        print("You have won "+ str(bet*35)  + " amount of dollars!!")
        return (bet*35)
    else:
        print("You have lost" + str(bet) + " amount of dollars!!")
        return -bet
