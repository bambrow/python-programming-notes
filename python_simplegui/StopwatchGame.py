# template for "Stopwatch: The Game"

# define global variables

import simpleguitk as simplegui
t = 0
total = 0
success = 0
timerstop = True

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def pformat(t):
    minute = (t // 10) // 60
    minisecond = t % 10
    second = (t // 10) % 60
    if minute < 10:
        sminute = '0' + str(minute)
    else:
        sminute = str(minute)
    if second < 10:
        ssecond = '0' + str(second)
    else:
        ssecond = str(second)
    time =  sminute + ':' + ssecond + '.' + str(minisecond)
    return time
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global timerstop
    timerstop = False
    timer.start()
    
def stop():
    global t, total, success, timerstop
    if t % 10 == 0 and t != 0 and timerstop == False:
        success += 1
        total += 1
    elif t % 10 != 0 and timerstop == False:
        total += 1
    else:
        total = total
    timerstop = True
    timer.stop()
    
def reset():
    global t, total, success, timerstop
    t = 0
    total = 0
    success = 0
    timerstop = True
    timer.stop()

# define event handler for timer with 0.1 sec interval
def count():
    global t
    t += 1
    if (t // 10) // 60 == 60:
        t = 0

# define draw handler
def draw(canvas):
    canvas.draw_text(pformat(t), [30, 120], 50, 'White')
    canvas.draw_text(str(success) + '/' + str(total), [135, 30], 25, 'Green')
    
# create frame
frame = simplegui.create_frame('Stopwatch Game', 200, 200)
frame.set_draw_handler(draw)
bstart = frame.add_button('Start', start, 100)
btop = frame.add_button('Stop', stop, 100)
breset = frame.add_button('Reset', reset, 100)

# register event handlers
timer = simplegui.create_timer(100, count)

# start frame
frame.start()

# Please remember to review the grading rubric
