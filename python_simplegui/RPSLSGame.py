# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def name_to_number(name):
    # delete the following pass statement and fill in your code below
    if name == 'rock':
        num = 0
    elif name == 'Spock':
        num = 1
    elif name == 'paper':
        num = 2
    elif name == 'lizard':
        num = 3
    elif name == 'scissors':
        num = 4
    else:
        print("Error! Incorrect name!")
    return num

    # convert name to number using if/elif/else
    # don't forget to return the result!


def number_to_name(number):
    # delete the following pass statement and fill in your code below
    if number == 0:
        name = 'rock'
    elif number == 1:
        name = 'Spock'
    elif number == 2:
        name = 'paper'
    elif number == 3:
        name = 'lizard'
    elif number == 4:
        name = 'scissors'
    else:
        print("Error! Incorrect number!")
    return name
    
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    

def rpsls(player_choice): 
    # delete the following pass statement and fill in your code below
    print(" ")
    # print a blank line to separate consecutive games
    print("Player chooses", player_choice)
    # print out the message for the player's choice
    player_number = name_to_number(player_choice)
    # convert the player's choice to player_number using the function name_to_number()
    import random
    comp_number = random.randrange(0, 5)
    # compute random guess for comp_number using random.randrange()
    comp_choice = number_to_name(comp_number)
    # convert comp_number to comp_choice using the function number_to_name()
    print("Computer chooses", comp_choice)
    # print out the message for computer's choice
    if (comp_number + 1) % 5 == player_number:
        print("Player wins!")
    elif (comp_number + 2) % 5 == player_number:
        print("Player wins!")
    elif comp_number == player_number:
        print("Player and computer tie!")
    else:
        print("Computer wins!")
    # compute difference of comp_number and player_number modulo five
    # use if/elif/else to determine winner, print winner message

    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric
