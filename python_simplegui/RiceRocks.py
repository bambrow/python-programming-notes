# program template for Spaceship
import simpleguitk as simplegui
import math
import random

# globals for user interface
WIDTH = 800
HEIGHT = 600
score = 0
lives = 3
time = 0
rock_max = 12
started = False

class ImageInfo:
    def __init__(self, center, size, radius = 0, lifespan = None, animated = False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated
    
# art assets created by Kim Lathrop, may be freely re-used in non-commercial projects, please credit Kim
    
# debris images - debris1_brown.png, debris2_brown.png, debris3_brown.png, debris4_brown.png
#                 debris1_blue.png, debris2_blue.png, debris3_blue.png, debris4_blue.png, debris_blend.png
debris_info = ImageInfo([320, 240], [640, 480])
debris_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png")

# nebula images - nebula_brown.png, nebula_blue.png
nebula_info = ImageInfo([400, 300], [800, 600])
nebula_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.f2014.png")

# splash image
splash_info = ImageInfo([200, 150], [400, 300])
splash_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/splash.png")

# ship image
ship_info = ImageInfo([45, 45], [90, 90], 35)
ship_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")

# missile image - shot1.png, shot2.png, shot3.png
missile_info = ImageInfo([5,5], [10, 10], 3, 50)
missile_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")

# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
asteroid_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")

# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")

# sound assets purchased from sounddogs.com, please do not redistribute
soundtrack = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
missile_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
missile_sound.set_volume(.5)
ship_thrust_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
explosion_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")

# alternative upbeat soundtrack by composer and former IIPP student Emiel Stopler
# please do not redistribute without permission from Emiel at http://www.filmcomposer.nl
#soundtrack = python_simplegui.load_sound("https://storage.googleapis.com/codeskulptor-assets/ricerocks_theme.mp3")

# helper functions to handle transformations
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]

def dist(p,q):
    return math.sqrt((p[0] - q[0]) ** 2+(p[1] - q[1]) ** 2)

# Ship class_basics
class Ship:
    def __init__(self, pos, vel, angle, image, info):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        
    def draw(self, canvas):
        global started
        if started and self.thrust:
            canvas.draw_image(self.image, [130, 45], self.image_size, self.pos, self.image_size, self.angle)
        else:
            canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)

    def update(self):
        friction = 0.01
        basicspeed = 0.10
        self.angle += self.angle_vel
        self.pos[0] = (self.pos[0] + self.vel[0]) % WIDTH
        self.pos[1] = (self.pos[1] + self.vel[1]) % HEIGHT
        self.vel[0] *= (1 - friction)
        self.vel[1] *= (1 - friction)
        if self.thrust:
            vector = angle_to_vector(self.angle)
            self.vel[0] += vector[0] * basicspeed
            self.vel[1] += vector[1] * basicspeed
            ship_thrust_sound.play()
        else:
            ship_thrust_sound.pause()
            ship_thrust_sound.rewind()
    
    def shoot(self):
        global missile_group
        vector = angle_to_vector(self.angle)
        missile_pos = [self.pos[0] + vector[0] * self.radius, self.pos[1] + vector[1] * self.radius]
        missile_vel = [self.vel[0] + vector[0] * 5, self.vel[1] + vector[1] * 5]
        a_missile = Sprite(missile_pos, missile_vel, self.angle, 0, missile_image, missile_info, missile_sound)
        missile_group.add(a_missile)
        
    def get_position(self):
        return self.pos
    
    def get_radius(self):
        return self.radius
    
# Sprite class_basics
class Sprite:
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        if sound:
            sound.rewind()
            sound.play()
   
    def draw(self, canvas):
        if self.animated:
            canvas.draw_image(self.image, [self.image_center[0] + self.image_size[0] * self.age, self.image_center[1]], self.image_size, self.pos, self.image_size, self.angle)
        else:
            canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)
    
    def update(self):
        self.angle += self.angle_vel
        self.pos[0] = (self.pos[0] + self.vel[0]) % WIDTH
        self.pos[1] = (self.pos[1] + self.vel[1]) % HEIGHT
        self.age += 1
        if self.age < self.lifespan:
            return False
        else:
            return True
    
    def collide(self, other_object):
        if dist(self.pos, other_object.get_position()) < self.radius + other_object.get_radius():
            return True
        else:
            return False
    
    def get_position(self):
        return self.pos
    
    def get_radius(self):
        return self.radius

def keydown(key):
    global started
    if started:
        if key == simplegui.KEY_MAP['left']:
            my_ship.angle_vel -= 0.05
        elif key == simplegui.KEY_MAP['right']:
            my_ship.angle_vel += 0.05
        elif key == simplegui.KEY_MAP['up']:
            my_ship.thrust = True
        elif key == simplegui.KEY_MAP['space']:
            my_ship.shoot()

def keyup(key):
    global started
    if started:
        if key == simplegui.KEY_MAP['left']:
            my_ship.angle_vel += 0.05
        elif key == simplegui.KEY_MAP['right']:
            my_ship.angle_vel -= 0.05
        elif key == simplegui.KEY_MAP['up']:
            my_ship.thrust = False  

# mouseclick handlers that reset UI and conditions whether splash image is drawn
def click(pos):
    global started, score, lives
    center = [WIDTH / 2, HEIGHT / 2]
    size = splash_info.get_size()
    inwidth = (center[0] - size[0] / 2) < pos[0] < (center[0] + size[0] / 2)
    inheight = (center[1] - size[1] / 2) < pos[1] < (center[1] + size[1] / 2)
    if (not started) and inwidth and inheight:
        started = True
        score = 0
        lives = 3
        ship_thrust_sound.rewind()
        explosion_sound.rewind()
        missile_sound.rewind()
        soundtrack.rewind()
        explosion_sound.rewind()
        soundtrack.play()

def draw(canvas):
    global my_ship, time, lives, score, started, rock_group, missile_group, explosion_group
    # animiate background
    time += 1
    wtime = (time / 4) % WIDTH
    center = debris_info.get_center()
    size = debris_info.get_size()
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
    canvas.draw_image(debris_image, center, size, (wtime - WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    canvas.draw_image(debris_image, center, size, (wtime + WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))

    # draw ship and sprites
    my_ship.draw(canvas)
    
    # update ship and sprites
    my_ship.update()
    process_sprite_group(rock_group, canvas)
    process_sprite_group(missile_group, canvas)
    process_sprite_group(explosion_group, canvas)
    
    score += group_group_collide(rock_group, missile_group) * 10
    
    if group_collide(rock_group, my_ship):
        lives -= 1
    if lives == 0:
        started = False
        soundtrack.pause()
        my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 0, ship_image, ship_info)
        rock_group = set([])
        missile_group = set([])
    
    canvas.draw_text('Lives: '+ str(lives), (30, 40), 30, "White")
    canvas.draw_text('Score: '+ str(score), (650, 40), 30, "White")
    
    # draw splash screen if not started
    if not started:
        canvas.draw_image(splash_image, splash_info.get_center(), 
                          splash_info.get_size(), [WIDTH / 2, HEIGHT / 2], 
                          splash_info.get_size())
            
# timer handler that spawns a rock    
def rock_spawner():
    global rock_group, rock_max, started, my_ship, score
    velocity_parameter_x = (random.random() + 0.3 + float(score) / 400.0) * random.choice([1, -1])
    velocity_parameter_y = (random.random() + 0.3 + float(score) / 400.0) * random.choice([1, -1])
    a_rock = Sprite([random.randrange(WIDTH), random.randrange(HEIGHT)], [velocity_parameter_x, velocity_parameter_y], 0, random.random() * 0.10 * random.choice([1, -1]), asteroid_image, asteroid_info)
    if started and len(rock_group) < rock_max and dist(a_rock.pos, my_ship.pos) > a_rock.radius + my_ship.radius + 50:
        rock_group.add(a_rock)
        
def process_sprite_group(group, canvas):
    for item in set(group):
        if item.update():
            group.remove(item)
        else:
            item.draw(canvas)
        
def group_collide(group, other_object):
    global explosion_group
    for item in set(group):
        if item.collide(other_object):
            an_explosion = Sprite(item.pos, [0, 0], 0, 0, explosion_image, explosion_info)
            explosion_group.add(an_explosion)
            explosion_sound.rewind()
            explosion_sound.play()
            group.discard(item)
            return True
    return False

def group_group_collide(group1, group2):
    collide_elements = 0
    for item in set(group1):
         if group_collide(group2, item):
            group1.discard(item)
            collide_elements += 1
    return collide_elements
    
# initialize frame
frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)

# initialize ship and two sprites
my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 0, ship_image, ship_info)
rock_group = set([])
missile_group = set([])
explosion_group = set([])

# register handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.set_mouseclick_handler(click)
timer = simplegui.create_timer(1000.0, rock_spawner)

# get things rolling
timer.start()
frame.start()