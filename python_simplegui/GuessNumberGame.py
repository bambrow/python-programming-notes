# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import random
import math
import simpleguitk as simplegui

secret_number = 0
guess_num = 0
num_range = 100

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number
    global guess_num
    global num_range
    if num_range == 100:
        guess_num = 7
    if num_range == 1000:
        guess_num = 10
    secret_number = random.randrange(0, num_range)
    print("New game.")
    print("Range: 0 to", num_range, ".")
    print("Chances left:", guess_num, ".")

# define event handlers for control panel
def range100():
    global num_range
    # button that changes the range to [0,100) and starts a new game 
    num_range = 100
    new_game()
    
def range1000():
    global num_range
    # button that changes the range to [0,1000) and starts a new game     
    num_range = 1000
    new_game()
    
def input_guess(guess):
    global secret_number
    global guess_num
    # main game logic goes here	
    guess = int(guess)
    print("Player guessed", guess, ".")
    guess_num = guess_num - 1
    if guess == secret_number:
        print("Congratulations! Correct!")
        new_game()
    if guess > secret_number:
        print("Your guess is higher!")
        print("Chances left:", guess_num, ".")
    if guess < secret_number:
        print("Your guess is lower!")
        print("Chances left:", guess_num, ".")
    if guess_num == 0:
        print("All chances were used up. Game over.")
        new_game()
          
# create frame
frame = simplegui.create_frame("Guess The Number", 200, 200)

# register event handlers for control elements and start frame
b100 = frame.add_button("Range is [0, 100)", range100, 150)
b1000 = frame.add_button("Range is [0, 1000)", range1000, 150)	
inp = frame.add_input("Enter your guess:", input_guess, 150)

# call new_game 
new_game()

# always remember to check your completed program against the grading rubric
