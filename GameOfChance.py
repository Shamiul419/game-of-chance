import random

print("Welcome to the game of chance.")
money = 100
#Prints money.
print("---------------------------------")
print("You have "+ str(money)+ " bucks." )
print("---------------------------------")
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
##The Card game.
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

##The even and odds game.
def cho_han(guess,bet):
    print("-----------------------------")
    print("Let's play a dice game.")
    print("-----------------------------")
#Checks if your bet is greater than 0.
    if bet <= 0:
        print("Your bet should be greater than 0.")
        return 0
    print("You have chosen " + str(guess) +" and bet " + str(bet) +" amount of dollars.")
#Genarates the number.
    first_dice = random.randint(1,6)
    second_dice = random.randint(1,6)
    total_number=first_dice + second_dice
    average=total_number%2
#Starts the game.
    if average ==0 and guess == "Even":
        print("You have won!!")
        return +bet
    elif average % 2 !=0 and guess == "Odd":
        print("You have won!!")
        return +bet
    else:
        print("The result was "+ str(average) +" .")
        print("You have lost")
##The Roulette game.
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
        print("Your Guess is " + str(guess))
        print("The wheel landed on " + str(number))
#More rules.
    if guess == "Even" and number % 2 ==0 and number != 0:
        print(str(number) + " is a Even number.")
        print("You have won " + str(bet) + " amount of dollars!!!")
        return -bet
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
        print("You have lost " + str(bet) + " amount of dollars!!")
        return -bet

##Calls the Coin flip game.
flip_rounds_wanna_play=int(input("How many coin flip rounds do you wanna play?"))
if flip_rounds_wanna_play == 0:
    print("You have skipped the coin flip game.")
elif flip_rounds_wanna_play >= 1:
    for i in range(flip_rounds_wanna_play):
        coin_flip_bet=int(float(input("How much do you want to bet?")))
        if coin_flip_bet <= money:
            coin_flip_guess=int(input("What is your guess?"))
            if 1 <= coin_flip_guess <= 2:
                flip_function(coin_flip_guess,coin_flip_bet)
            else:
                print("Enter between 1 and 2.")
        else:
            print("You dont have that much money,son.")

##Calls the Card Game.
cards_rounds_wanna_play=int(input("How many cards game do you wanna play?"))
if cards_rounds_wanna_play == 0:
    print("You have skipped the cards game.")
elif cards_rounds_wanna_play >= 1:
    for i in range(cards_rounds_wanna_play):
        cards_bet=int(float(input("How much do you wanna bet?")))
        if cards_bet <= money:
            card_game(cards_bet)
        else:
            print("You dont have that much money,son.")
##Calls the even and odds game.
cho_han_rounds_wanna_play=int(input("How many even and odds round do you want to play?"))
if cho_han_rounds_wanna_play==0:
    print("You have skipped even and odds game.")
elif cho_han_rounds_wanna_play>=1:
    for i in range((cho_han_rounds_wanna_play)):
        cho_han_bet=int(float(input("Whats your bet?")))
        if cho_han_bet <=money:
            cho_han_guess=input("What is your guess? Pick 'Even' or 'Odd'.")
            if cho_han_guess =="Even" and cho_han_guess == "Odd":
                cho_han(cho_han_guess,cho_han_bet)
            else:
                print("Please pick between 'Even' and 'Odd'")
        else:
            print("You dont have that much money,son.")

##Calls the Roulette game.
roulette_rounds_wanna_play=int(input("How many roulette rounds do you want to play?"))
if roulette_rounds_wanna_play == 0:
    print("You have skipped the roulette game.")
elif roulette_rounds_wanna_play >= 1:
    roulette_bet=int(float(input("How much do you want to bet?")))
    if roulette_bet <= money:
        roulette_guess=int(input("What is your guess? Choose between 1 and 37."))
        if 1<= roulette_guess <= 37:
            roulette(roulette_guess,roulette_bet)
        else:
            print("Enter a valid number between 1 and 37.")
    else:
        print("You dont have that much money,son.")
