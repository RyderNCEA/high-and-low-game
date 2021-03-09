import random

#Generate messages with a style border
def statement_generator(text, symbol):
    length = len(text)+6
    print(symbol*length)
    print(symbol*2 + " "*(len(text)+2) + symbol*2)    
    print(symbol*2 + " " + text + " " + symbol*2)   
    print(symbol*2 + " "*(len(text)+2) + symbol*2)
    print(symbol*length)

def getGuess():
    while True:
        try:
            user_guess = int(input("What is your guess? "))
            if user_guess > 0:
                return user_guess
        except:
            print("Invalid Input, enter a number.")
            continue

def start_game():
    statement_generator("Welcome to High and Low", "=")

    #Ask user if they have played before, if no display playing info
    played_before = input("Have you played the game before? [y]/[n]: ")
    #Make sure input is valid
    while played_before != "n" and played_before != "y":
        print("Invalid Input, use [y] or [n]!")
        played_before = input("Have you played the game before? [y]/[n]: ")
    if played_before == "n":
        print("\nA random number between 1 - 100 will be generated.")
        print("You must try guess this number in 9 guesses.\n")
        print("The game will tell you if your guess is too low or too high.\n")

    #Determine how many rounds to play
    while True:
        playing_rounds = input("How many rounds do you want to play? [infinite] or [a number]: ")
        if playing_rounds == "infinite":
            playing_rounds = 9999999999
            break
        try:
            playing_rounds = int(playing_rounds)
            if playing_rounds < 1:
                print("Invalid Input, use a number higher than 1!")
                continue
            else:
                break
        except:
            continue
    
    while playing_rounds > 0:
        statement_generator("Starting Round","=")
        guesses = []
        secret_number = random.randint(1, 100)
        playing_rounds += -1
        user_guess = getGuess()
        while len(guesses) < 9:
            if int(secret_number) < int(user_guess):
                print("The secret number is lower!\n")
                guesses.append(user_guess)
                user_guess = getGuess()
                continue

            elif int(secret_number) > int(user_guess):
                print("The secret number is higher!\n")
                guesses.append(user_guess)
                user_guess = getGuess()
                continue

            else:
                print("You have guessed the number, it was {}".format(str(secret_number)))
                break
            

start_game()
