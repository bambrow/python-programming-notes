# implementation of card game - Memory

import simpleguitk as simplegui
import random

# helper function to initialize globals
def new_game():
    global numbers, exposed, clicks, moves, turns
    numbers = range(8) * 2
    random.shuffle(numbers)
    exposed = [False] * 16
    clicks = 0
    turns = 0
         
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global clicks, turns, temp1, temp2
    card = pos[0] // 50
    if exposed[card] == False:
        if clicks == 0:
            temp1 = card
            exposed[card] = True
            clicks = 1
        elif clicks == 1:
            temp2 = card
            exposed[card] = True
            clicks = 2
            turns += 1
        elif clicks == 2:
            if numbers[temp1] == numbers[temp2]:
                pass
            else:
                exposed[temp1] = False
                exposed[temp2] = False
            temp1 = card
            exposed[card] = True
            clicks = 1
    else:
        pass
                          
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global numbers, exposed, turns
    for i in range(16):
        if exposed[i] == True:
            canvas.draw_text(str(numbers[i]), (i*50+15, 70), 50, "White")
        else:
            canvas.draw_polygon([[i*50, 0], [(i+1)*50, 0], [(i+1)*50, 100], [i*50, 100]], 1, "Black", "Green")
    label.set_text("Turns = " + str(turns))
    
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()

# Always remember to review the grading rubric