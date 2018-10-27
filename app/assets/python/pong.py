# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

class Ball:
    """ A representation of a ball with a position (pos) and a velocity (vel). """
    def __init__(self, x, y):
        self.pos = [WIDTH / 2, HEIGHT /2]
        self.vel = [x, y]
            
    """ Check if the ball has collided with the top or bottom 
        of the play field and change the velocity accordingly. """
    def hit_top_or_bottom(self):
        if self.pos[1] - BALL_RADIUS < 0 or self.pos[1] + BALL_RADIUS > HEIGHT:
            self.vel[1] *= -1
            
    """ Check if the ball has collided with either gutter and, if so, spawn a
        new ball headed towards the opposite player. """
    def hit_gutter(self):
        # Find the top and bottom of each player's paddle at the time this method is invoked.
        p1_top = player1.pos[1] - HALF_PAD_HEIGHT
        p1_bottom = player1.pos[1] + HALF_PAD_HEIGHT
        p2_top = player2.pos[1] - HALF_PAD_HEIGHT
        p2_bottom = player2.pos[1] + HALF_PAD_HEIGHT
        
        # If Ball is hitting either gutter, we will have one and only one 
        # of the below variables True. Otherwise, they will both be False.
        hitting_left_gutter = self.pos[0] - BALL_RADIUS - PAD_WIDTH < 0
        hitting_right_gutter = self.pos[0] + BALL_RADIUS + PAD_WIDTH > WIDTH
        
        if hitting_left_gutter:
            if self.pos[1] + BALL_RADIUS > p1_top and self.pos[1] - BALL_RADIUS < p1_bottom:
                self.vel[0] *= -1.1
            else:
                global score2
                score2 += 1
                spawn_ball(RIGHT)
        elif hitting_right_gutter:
            if self.pos[1] + BALL_RADIUS > p2_top and self.pos[1] - BALL_RADIUS < p2_bottom:
                self.vel[0] *= -1.1
            else:
                global score1
                score1 += 1
                spawn_ball(LEFT)
            
class Paddle:
    """ A representation of a player's paddle that can be placed at any given x location. """
    def __init__(self, x):
        self.pos = [x + HALF_PAD_WIDTH, HEIGHT / 2]
        self.vel = [0, 0]
       
    """ Checks if paddle's position has met the top or bottom of the playfield.
    If the paddle has reached one of these edges, it is pushed back into play and its
    velocity set to 0. Otherwise, the paddles pos is updated with the current vel. """
    def reached_top_or_bottom(self):
        at_top = self.pos[1] - HALF_PAD_HEIGHT <= 0
        at_bottom = self.pos[1] + HALF_PAD_HEIGHT >= HEIGHT
    
        if not at_top and not at_bottom:
            self.pos[1] += self.vel[1]
        elif at_top:
            self.pos[1] += 1
            self.vel[1] = 0
        elif at_bottom:
            self.pos[1] -= 1
            self.vel[1] = 0

""" Initialize ball_pos and ball_vel for new ball in middle of table.
If direction is RIGHT, the ball's velocity sends it towards the 
upper right, otherwise, the upper left. """
def spawn_ball(direction):
    global ball
    
    # The local value x will determine the direction and speed the spawned ball will take.
    x = random.randrange(-5, -2)
    if direction:
        x *= -1
    
    # The local value y will determine the angle of the spawned ball.
    y = random.randrange(-4, -1)
    
    ball = Ball(x, y)


# define event handlers
def new_game():
    global score1, score2  # these are ints
    global player1, player2
    
    score1, score2 = 0, 0
    spawn_ball(RIGHT)
    player1 = Paddle(0)
    player2 = Paddle(WIDTH - PAD_WIDTH)

def draw(canvas):
    global score1, score2
    
    # draw scores
    canvas.draw_text(str(score1), [WIDTH / 4, HEIGHT / 4], 64, "White")
    canvas.draw_text(str(score2), [(3 * WIDTH) / 4, HEIGHT / 4], 64, "White")
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball.pos[0] += ball.vel[0]
    ball.pos[1] += ball.vel[1]
    ball.hit_top_or_bottom()
    
    # determine whether paddle and ball collide
    ball.hit_gutter() 
            
    # draw ball
    canvas.draw_circle(ball.pos, BALL_RADIUS, 1, "White", "White")
    
    # update paddle's vertical position, keep paddle on the screen
    player1.reached_top_or_bottom()
    player2.reached_top_or_bottom()
    
    # draw paddles
    # Player1's paddle
    canvas.draw_line([player1.pos[0], player1.pos[1] - HALF_PAD_HEIGHT], 
                     [player1.pos[0], player1.pos[1] + HALF_PAD_HEIGHT], 
                     PAD_WIDTH, "White")
    
    # Player2's paddle
    canvas.draw_line([player2.pos[0], player2.pos[1] - HALF_PAD_HEIGHT], 
                     [player2.pos[0], player2.pos[1] + HALF_PAD_HEIGHT], 
                     PAD_WIDTH, "White")    
        
def keydown(key):
    acc = 5
    
    if key == simplegui.KEY_MAP["w"]:
        player1.vel[1] -= acc
    elif key == simplegui.KEY_MAP["up"]:
        player2.vel[1] -= acc
    elif key == simplegui.KEY_MAP["s"]:
        player1.vel[1] += acc
    elif key == simplegui.KEY_MAP["down"]:
        player2.vel[1] += acc
        
def keyup(key):    
    if key == simplegui.KEY_MAP["w"]:
        player1.vel[1] = 0
    elif key == simplegui.KEY_MAP["up"]:
        player2.vel[1] = 0
    elif key == simplegui.KEY_MAP["s"]:
        player1.vel[1] = 0
    elif key == simplegui.KEY_MAP["down"]:
        player2.vel[1] = 0

# create frame
frame = simplegui.create_frame("Pong!", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Reset", new_game, 100)


# start frame
new_game()
frame.start()