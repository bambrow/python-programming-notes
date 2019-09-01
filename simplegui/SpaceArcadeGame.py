"""
Created by Bambrow
https://github.com/bambrow
April 2016
"""
import simplegui
import math
import random

# globals for user interface
WIDTH = 800
HEIGHT = 600
score = 0
lives = 3
time = 0
started = False
power_text = " "

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
debris_image1 = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris3_brown.png")
debris_image2 = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris4_blue.png")

# nebula images - nebula_brown.png, nebula_blue.png
nebula_info = ImageInfo([400, 300], [800, 600])
nebula_image1 = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.png")
nebula_image2 = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_brown.png")

# splash image
splash_info = ImageInfo([200, 150], [400, 300])
splash_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/splash.png")

# ship image
ship_info = ImageInfo([45, 45], [90, 90], 35)
ship_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")

# missile image - shot1.png, shot2.png, shot3.png
missile_info = ImageInfo([5,5], [10, 10], 3)
power_info = ImageInfo([10,10], [20, 20], 7)
missile_image1 = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot1.png")
missile_image2 = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")
missile_image3 = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot3.png")

# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
asteroid_image1 = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")
asteroid_image2 = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_brown.png")
asteroid_image3 = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blend.png")

# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
explosion_image1 = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_orange.png")
explosion_image2 = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_blue.png")
explosion_image3 = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_blue2.png")
explosion_image4 = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")

# sound assets purchased from sounddogs.com, please do not redistribute
# soundtrack = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
missile_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
missile_sound.set_volume(.2)
ship_thrust_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
ship_thrust_sound.set_volume(.1)
explosion_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")
explosion_sound.set_volume(.5)

# alternative upbeat soundtrack by composer and former IIPP student Emiel Stopler
# please do not redistribute without permission from Emiel at http://www.filmcomposer.nl
soundtrack = simplegui.load_sound("https://storage.googleapis.com/codeskulptor-assets/ricerocks_theme.mp3")

# helper functions to handle transformations
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]

def dist(p,q):
    return math.sqrt((p[0] - q[0]) ** 2+(p[1] - q[1]) ** 2)

# Ship class_basics
class Ship:
    def __init__(self, pos, vel, image, info):
        self.pos = [pos[0],pos[1]]
        self.vel = vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.rank = 2
        
    def draw(self, canvas):
        global started
        if started:
            canvas.draw_image(self.image, [130, 45], self.image_size, self.pos, self.image_size, 0)

    def update(self):
        global started, time
        if started:
            self.pos[1] = (self.pos[1] + self.vel) % HEIGHT
            if time % 20 == 0:
                self.shoot()
    
    def shoot(self):
        global missile_group
        missile_pos = [self.pos[0] + self.radius, self.pos[1]]
        missile_vel = [5, 0]
        if self.rank == 1:
            missile_group.add(Sprite(missile_pos, missile_vel, 0, 0, missile_image1, missile_info, missile_sound))
        elif self.rank == 2:
            missile_group.add(Sprite([missile_pos[0], missile_pos[1] - 15], missile_vel, 0, 0, missile_image1, missile_info, missile_sound))
            missile_group.add(Sprite([missile_pos[0], missile_pos[1] + 15], missile_vel, 0, 0, missile_image1, missile_info))
        elif self.rank == 3:
            missile_group.add(Sprite(missile_pos, missile_vel, 0, 0, missile_image1, missile_info, missile_sound))
            missile_group.add(Sprite([missile_pos[0], missile_pos[1] - 20], missile_vel, 0, 0, missile_image1, missile_info))
            missile_group.add(Sprite([missile_pos[0], missile_pos[1] + 20], missile_vel, 0, 0, missile_image1, missile_info))
        elif self.rank == 4:
            missile_group.add(Sprite([missile_pos[0], missile_pos[1] - 15], missile_vel, 0, 0, missile_image1, missile_info, missile_sound))
            missile_group.add(Sprite([missile_pos[0], missile_pos[1] + 15], missile_vel, 0, 0, missile_image1, missile_info))
            missile_group.add(Sprite([missile_pos[0], missile_pos[1] - 20], [missile_vel[0], missile_vel[1] - 1], 0, 0, missile_image1, missile_info))
            missile_group.add(Sprite([missile_pos[0], missile_pos[1] + 20], [missile_vel[0], missile_vel[1] + 1], 0, 0, missile_image1, missile_info))
        elif self.rank == 5:
            missile_group.add(Sprite(missile_pos, missile_vel, 0, 0, missile_image1, missile_info, missile_sound))
            missile_group.add(Sprite([missile_pos[0], missile_pos[1] - 20], missile_vel, 0, 0, missile_image1, missile_info))
            missile_group.add(Sprite([missile_pos[0], missile_pos[1] + 20], missile_vel, 0, 0, missile_image1, missile_info))
            missile_group.add(Sprite([missile_pos[0], missile_pos[1] - 25], [missile_vel[0], missile_vel[1] - 1], 0, 0, missile_image1, missile_info))
            missile_group.add(Sprite([missile_pos[0], missile_pos[1] + 25], [missile_vel[0], missile_vel[1] + 1], 0, 0, missile_image1, missile_info))            
            
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
        self.pos[0] = (self.pos[0] + self.vel[0])
        self.pos[1] = (self.pos[1] + self.vel[1])
        self.age += 1
        self.special_ability()
        if self.pos[0] < -10 or self.pos[1] < -10 or self.pos[0] > WIDTH + 20 or self.pos[1] > HEIGHT + 10 or self.age >= self.lifespan:
            return True
        else:
            return False
        
    def special_ability(self):
        pass
        
    def collide(self, other_object):
        if dist(self.pos, other_object.get_position()) < self.radius + other_object.get_radius():
            return True
        else:
            return False
    
    def get_position(self):
        return self.pos
    
    def get_radius(self):
        return self.radius

# SpriteRock class_basics
class SpriteRock(Sprite):
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
        self.shot = False
        if sound:
            sound.rewind()
            sound.play()
        
    def special_ability(self):
        if self.shot == False and WIDTH * 0.7 < self.pos[0] < WIDTH * 0.8:
            self.shoot()
            
    def shoot(self):
        global enemy_missile_group, my_ship
        missile_pos = [self.pos[0] - self.radius, self.pos[1]]
        if 0 <= score <= 500:
            missile_vel = [-(missile_pos[0] - my_ship.pos[0]) / 175.0, -(missile_pos[1] - my_ship.pos[1]) / 175.0]
        elif score <= 1000:
            missile_vel = [-(missile_pos[0] - my_ship.pos[0]) / 135.0, -(missile_pos[1] - my_ship.pos[1]) / 135.0]
        elif score <= 2500:
            missile_vel = [-(missile_pos[0] - my_ship.pos[0]) / 100.0, -(missile_pos[1] - my_ship.pos[1]) / 100.0]
        else:
            missile_vel = [-(missile_pos[0] - my_ship.pos[0]) / 75.0, -(missile_pos[1] - my_ship.pos[1]) / 75.0]
        enemy_missile_group.add(Sprite(missile_pos, missile_vel, 0, 0, missile_image2, missile_info))
        self.shot = True

# SpritePower class_basics
class SpritePower(Sprite):
    def draw(self, canvas):
        image_size = [0,0]
        image_size[0] = self.image_size[0] * 2
        image_size[1] = self.image_size[1] * 2
        canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, image_size, self.angle)

# SpriteSuperRock class_basics
class SpriteSuperRock(Sprite):
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None, lives = 9):
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
        self.lives = lives
        if sound:
            sound.rewind()
            sound.play()
        
    def special_ability(self):
        global time
        if time % 60 == 0:
            self.shoot()
        if self.pos[0] <= 700:
            self.vel[0] = 0
        if self.pos[1] <= 100 or self.pos[1] >= 500:
            self.vel[1] = -self.vel[1]
    
    def shoot(self):
        global enemy_missile_group
        missile_pos = [self.pos[0] - self.radius, self.pos[1]]
        if 0 <= score <= 2000:
            missile_vel = [-4, 0]
        else:
            missile_vel = [-7, 0]
        enemy_missile_group.add(Sprite(missile_pos, missile_vel, 0, 0, missile_image2, missile_info))
        enemy_missile_group.add(Sprite([missile_pos[0], missile_pos[1] - 15], [missile_vel[0], missile_vel[1] - 1], 0, 0, missile_image2, missile_info))
        enemy_missile_group.add(Sprite([missile_pos[0], missile_pos[1] + 15], [missile_vel[0], missile_vel[1] + 1], 0, 0, missile_image2, missile_info))
        enemy_missile_group.add(Sprite([missile_pos[0], missile_pos[1] - 30], [missile_vel[0], missile_vel[1] - 2], 0, 0, missile_image2, missile_info))
        enemy_missile_group.add(Sprite([missile_pos[0], missile_pos[1] + 30], [missile_vel[0], missile_vel[1] + 2], 0, 0, missile_image2, missile_info))
    
    def collide(self, other_object):
        if dist(self.pos, other_object.get_position()) < self.radius + other_object.get_radius():
            if self.lives >= 2:
                self.lives -= 1
                return 1 # collision, but not dead
            else:
                return 2 # collision and dead
        else:
            return 0 # no collision
        
def keydown(key):
    global started
    if started:
        if key == simplegui.KEY_MAP['up']:
            my_ship.vel -= 6
        elif key == simplegui.KEY_MAP['down']:
            my_ship.vel += 6
     
def keyup(key):
    global started
    if started:
        if key == simplegui.KEY_MAP['up']:
            my_ship.vel += 6
        elif key == simplegui.KEY_MAP['down']:
            my_ship.vel -= 6

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
        lives = 5
        ship_thrust_sound.rewind()
        explosion_sound.rewind()
        missile_sound.rewind()
        soundtrack.rewind()
        explosion_sound.rewind()
        soundtrack.play()
        rock_timer.start()
        power_timer.start()
        superrock_timer.start()

def draw(canvas):
    global my_ship, time, lives, score, started, rock_group, missile_group, explosion_group, enemy_missile_group, superrock_group, power_text
    # animiate background
    time += 1
    wtime = -(time * 2) % WIDTH
    center = debris_info.get_center()
    size = debris_info.get_size()
    canvas.draw_image(nebula_image1, nebula_info.get_center(), nebula_info.get_size(), [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
    canvas.draw_image(debris_image1, center, size, (wtime - WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    canvas.draw_image(debris_image1, center, size, (wtime + WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))

    # draw ship and sprites
    my_ship.draw(canvas)
    
    # update ship and sprites
    my_ship.update()
    process_sprite_group(rock_group, canvas)
    process_sprite_group(missile_group, canvas)
    process_sprite_group(explosion_group, canvas)
    process_sprite_group(enemy_missile_group, canvas)
    process_sprite_group(power_group, canvas)
    process_sprite_group(superrock_group, canvas)
    
    score_record()
    ship_update()
    
    canvas.draw_text('Lives: '+ str(lives), (30, 40), 30, "White")
    canvas.draw_text('Score: '+ str(score), (630, 40), 30, "White")
    canvas.draw_text(power_text, (310, 35), 25, "White", "monospace")
    
    # draw splash screen if not started
    if not started:
        canvas.draw_image(splash_image, splash_info.get_center(), 
                          splash_info.get_size(), [WIDTH / 2, HEIGHT / 2], 
                          splash_info.get_size())
            
# timer handlers
def rock_spawner():
    global rock_group, started, my_ship, score
    pos = [WIDTH + 20, random.randrange(HEIGHT)]
    velocity_x = -(random.random() + 0.8 + float(score) / 200.0)
    if velocity_x <= -8.5:
        velocity_x = -8.5
    velocity_y = (pos[1] - random.randrange(HEIGHT)) / ((pos[0] - my_ship.pos[0]) / velocity_x)
    if started:
        rock_group.add(SpriteRock(pos, [velocity_x, velocity_y], 0, random.random() * 0.10 * random.choice([1, -1]), asteroid_image1, asteroid_info))

def power_spawner():
    global power_group, started, time
    pos = [WIDTH + 20, random.randrange(HEIGHT)]
    vel = [-9, 0]
    if started:
        power_group.add(SpritePower(pos, vel, math.pi, 0, missile_image3, power_info))
   
def superrock_spawner():
    global superrock_group, started
    pos = [WIDTH + 20, random.randrange(120, HEIGHT - 120)]
    vel = [-1, (random.random() * 3 + 0.8) * random.choice([1, -1])]
    if started and len(superrock_group) == 0:
        superrock_group.add(SpriteSuperRock(pos, vel, 0, random.random() * 0.10 * random.choice([1, -1]), asteroid_image2, asteroid_info, lives = 9))

# score recorder
def score_record():
    global score, rock_group, missile_group, superrock_group
    score += group_group_collide(missile_group, rock_group) * 8
    score += group_superrock_collide(missile_group, superrock_group) * 5

def ship_update():
    global rock_group, my_ship, enemy_missile_group, missile_group, power_group, superrock_group, lives, started, time, score, power_text
    if group_collide(rock_group, my_ship) or group_collide(enemy_missile_group, my_ship):
        lives -= 1
        rock_group = set([])
        missile_group = set([])
        enemy_missile_group = set([])
        if my_ship.rank >= 2:
            my_ship.rank -= 1
        power_text = " "
    if power_collide(power_group, my_ship):
        if time % 2 == 0:
            if my_ship.rank >= 5:
                score += 200
                power_text = "Score + 200"
            else:
                my_ship.rank += 1
                power_text = "Power + 1"
        else:
            if lives >= 10:
                score += 200
                power_text = "Score + 200"
            else:
                lives += 1
                power_text = "Life + 1"
    if lives == 0:
        started = False
        time = 0
        soundtrack.pause()
        my_ship = Ship([ship_info.radius, HEIGHT / 2], 0, ship_image, ship_info)
        rock_group = set([])
        enemy_missile_group = set([])
        power_group = set([])
        superrock_group = set([])
        rock_timer.stop()
        power_timer.stop()
        superrock_timer.stop()
        power_text = " "

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
            explosion_group.add(Sprite(item.pos, [0, 0], 0, 0, explosion_image1, explosion_info))
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

def superrock_collide(group, other_object):
    global explosion_group
    for item in set(group):
        if item.collide(other_object) == 1:
            return 1
        elif item.collide(other_object) == 2:
            explosion_group.add(Sprite(item.pos, [0, 0], 0, 0, explosion_image1, explosion_info))
            explosion_sound.rewind()
            explosion_sound.play()
            group.discard(item)
            return 2
    return 0

def group_superrock_collide(group1, group2):
    collide_elements = 0
    for item in set(group1):
         if superrock_collide(group2, item):
            group1.discard(item)
            collide_elements += 1
    return collide_elements

def power_collide(group, other_object):
    for item in set(group):
        if item.collide(other_object):
            group.discard(item)
            return True
    return False
    
# initialize frame
frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)

# initialize ship and sprites
my_ship = Ship([ship_info.radius, HEIGHT / 2], 0, ship_image, ship_info)
rock_group = set([])
missile_group = set([])
explosion_group = set([])
enemy_missile_group = set([])
power_group = set([])
superrock_group = set([])

# register handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.set_mouseclick_handler(click)
rock_timer = simplegui.create_timer(1500.0, rock_spawner)
power_timer = simplegui.create_timer(10000.0, power_spawner)
superrock_timer = simplegui.create_timer(10000.0, superrock_spawner)

# start frame
frame.start()