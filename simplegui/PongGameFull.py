# Pong - Computer Version
"""
Created by Bambrow
https://github.com/bambrow
February 2016
"""

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 800
HEIGHT = 600       
BALL_RADIUS = 8
PAD_WIDTH = 8
PAD_HEIGHT = 100
LEFT = False
RIGHT = True
vel = 5
difficulty = 'easy'
auto = False
background_color = 'Black'
ball_color = 'White'
line_color = 'White'
paddle_color = 'White'
score_color = 'White'

# supported colors: 'Aqua''Black''Blue''Fuchsia''Gray''Green''Lime'
#                   'Maroon''Navy''Olive''Orange''Purple''Red'	      
#                   'Silver''Teal''White''Yellow'
# or general HTML color names: http://www.w3schools.com/colors/colors_names.asp

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel
    global LEFT, RIGHT
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    if direction == RIGHT:
        ball_vel = [random.randrange(160, 300) / 60.0, -(random.randrange(90, 250) / 60.0)]
    else:
        ball_vel = [-random.randrange(160, 300) / 60.0, -(random.randrange(90, 250) / 60.0)]
    
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel
    global score1, score2
    global LEFT, RIGHT
    paddle1_pos = (HEIGHT - PAD_HEIGHT) / 2
    paddle2_pos = (HEIGHT - PAD_HEIGHT) / 2
    paddle1_vel = 0
    paddle2_vel = 0
    score1 = 0
    score2 = 0
    direction = random.randrange(0, 2)
    if direction == 0:
        direction = LEFT
    else:
        direction = RIGHT
    spawn_ball(direction)
    

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    global LEFT, RIGHT, vel, paddle1_vel, paddle2_vel, difficulty, auto
    
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, line_color)
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, line_color)
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, line_color)
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    if ball_pos[1] >= (HEIGHT - BALL_RADIUS):
        ball_vel[1] = - ball_vel[1]
            
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, ball_color, ball_color)
    
    # update paddle's vertical position, keep paddle on the screen
    if -vel < paddle1_pos + paddle1_vel < 0:
        paddle1_pos = 0
    if HEIGHT - PAD_HEIGHT < paddle1_pos + paddle1_vel < HEIGHT - PAD_HEIGHT + vel:
        paddle1_pos = HEIGHT - PAD_HEIGHT # optimize paddle's position
    if -vel < paddle2_pos + paddle2_vel < 0:
        paddle2_pos = 0
    if HEIGHT - PAD_HEIGHT < paddle2_pos + paddle2_vel < HEIGHT - PAD_HEIGHT + vel:
        paddle2_pos = HEIGHT - PAD_HEIGHT # optimize paddle's position
    if 0 <= paddle1_pos + paddle1_vel <= HEIGHT - PAD_HEIGHT:
        paddle1_pos += paddle1_vel # update paddle's position
    if 0 <= paddle2_pos + paddle2_vel <= HEIGHT - PAD_HEIGHT:
        paddle2_pos += paddle2_vel # update paddle's position
    
    # draw paddles
    canvas.draw_line([PAD_WIDTH / 2, paddle1_pos], [PAD_WIDTH / 2, paddle1_pos + PAD_HEIGHT], PAD_WIDTH, paddle_color)
    canvas.draw_line([WIDTH - PAD_WIDTH / 2, paddle2_pos], [WIDTH - PAD_WIDTH / 2, paddle2_pos + PAD_HEIGHT], PAD_WIDTH, paddle_color)
    
    # difficulty definition
    if difficulty == 'easy':
        detection = WIDTH / 2
    if difficulty == 'normal' or difficulty == 'hard':
        detection = 3 * WIDTH / 4

    # update velocity of computer paddle
    if (auto == False and difficulty == 'hard') or (ball_pos[0] <= detection and ball_vel[0] < 0):
        if paddle1_pos + (4 * PAD_HEIGHT / 5) <= ball_pos[1]:
            paddle1_vel = vel
        elif paddle1_pos + PAD_HEIGHT / 5 >= ball_pos[1]:
            paddle1_vel = -vel
        else:
            paddle1_vel = ball_vel[1]
    else:
        paddle1_vel = 0

    # auto mode
    if auto == True:
        if ball_vel[0] < 0:
            if paddle1_pos + (3 * PAD_HEIGHT / 4) <= ball_pos[1]:
                paddle1_vel = vel
            elif paddle1_pos + PAD_HEIGHT / 4 >= ball_pos[1]:
                paddle1_vel = -vel
            else:
                paddle1_vel = ball_vel[1]
        else:
            paddle1_vel = 0
        if ball_vel[0] > 0:
            if paddle2_pos + (3 * PAD_HEIGHT / 4) <= ball_pos[1]:
                paddle2_vel = vel
            elif paddle2_pos + PAD_HEIGHT / 4 >= ball_pos[1] and ball_vel[0] > 0:
                paddle2_vel = -vel
            else:
                paddle2_vel = ball_vel[1]
        else:
            paddle2_vel = 0
    
    # determine whether paddle and ball collide and the velocity change
    if ball_pos[0] <= BALL_RADIUS + PAD_WIDTH:
        if paddle1_pos <= ball_pos[1] <= paddle1_pos + PAD_HEIGHT:
            ball_vel[0] = - 1.1 * ball_vel[0]
            if paddle1_pos <= ball_pos[1] <= paddle1_pos + PAD_HEIGHT / 8 or paddle1_pos + (7 * PAD_HEIGHT / 8) <= ball_pos[1] <= paddle1_pos + PAD_HEIGHT:
                ball_vel[1] = 1.1 * ball_vel[1]
        else:
            score2 += 1
            spawn_ball(RIGHT)
    if ball_pos[0] >= WIDTH - BALL_RADIUS - PAD_WIDTH:
        if paddle2_pos <= ball_pos[1] <= paddle2_pos + PAD_HEIGHT:
            ball_vel[0] = - 1.1 * ball_vel[0]
            if paddle2_pos <= ball_pos[1] <= paddle2_pos + PAD_HEIGHT / 8 or paddle2_pos + (7 * PAD_HEIGHT / 8) <= ball_pos[1] <= paddle2_pos + PAD_HEIGHT:
                ball_vel[1] = 1.1 * ball_vel[1]
        else:
            score1 += 1
            spawn_ball(LEFT)
               
    # draw scores
    canvas.draw_text(str(score1), (WIDTH / 2 - 55, HEIGHT / 8), 25, score_color)
    canvas.draw_text(str(score2), (WIDTH / 2 + 35, HEIGHT / 8), 25, score_color)
        
def keydown(key):
    global paddle2_vel, vel, auto
    if auto == False and key == simplegui.KEY_MAP["down"]:
        paddle2_vel = vel
    if auto == False and key == simplegui.KEY_MAP["up"]:
        paddle2_vel = -vel
   
def keyup(key):
    global paddle2_vel, auto
    if auto == False and key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0
    if auto == False and key == simplegui.KEY_MAP["up"]:
        paddle2_vel = 0

def easy_mode():
    global difficulty, auto
    difficulty = 'easy'
    auto = False
    new_game()
    
def normal_mode():
    global difficulty, auto
    difficulty = 'normal'
    auto = False
    new_game()

def hard_mode():
    global difficulty, auto
    difficulty = 'hard'
    auto = False
    new_game()
    
def computer_fight():
    global auto
    auto = True
    new_game()

def long_paddles():
    global PAD_HEIGHT
    PAD_HEIGHT = 180
    new_game()

def short_paddles():
    global PAD_HEIGHT
    PAD_HEIGHT = 100
    new_game()

# create frame
frame = simplegui.create_frame("Pong Game", WIDTH, HEIGHT)
frame.set_canvas_background(background_color)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button('Restart', new_game, 100)
frame.add_button('Easy Mode', easy_mode, 100)
frame.add_button('Normal Mode', normal_mode, 100)
frame.add_button('Hard Mode', hard_mode, 100)
frame.add_button('Computer Fight!', computer_fight, 150)
frame.add_button('Long Paddles', long_paddles, 150)
frame.add_button('Short Paddles', short_paddles, 150)

# start frame
new_game()
frame.start()
