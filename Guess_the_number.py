# guess the number
import random # we need to import the random function to choose the number
guess_number = random.randint(1,20) # system will choose the random numbers from 1 to 20

while True: #until the condition satisfied, it should continue hence while loop has been used
    user_guess = int(input()) #for user input
    if user_guess < guess_number: # check for the condition
        print("too low")
    elif user_guess > guess_number: # check for another condition
        print("too high")
    else: # if above conditions are not satisfied, then it will print for this condition
        print("Correct")
        break #to end the game
    