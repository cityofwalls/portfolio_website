import simplegui
import random

WIDTH = 600
HEIGHT = 400
BODY = 12
colors = ["Red", "Yellow", "Brown", "Pink", "Blue", "Orange"]

class Frog:
    """ Player controller frog character. """
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT - BODY
        
    def draw_frog(self, canvas):
        canvas.draw_line([self.x, self.y - BODY], 
                         [self.x, self.y + BODY], 
                         BODY, "Lime")
        
    def collide_with_car(self):
        for street in cars:
            for car in street:
                if self.y - BODY < car.y and self.y + BODY > car.y:
                    if self.x == car.x - BODY or self.x == car.x + BODY:
                        start_game()
                        
    def sitting_on_log(self):
        for path in logs:
            for log in path:
                log.has_frog = False
                if self.y - BODY < log.y and self.y + BODY > log.y:
                    if self.x > log.x - BODY and self.x < log.x + BODY:
                        log.has_frog = True
                        if log.number % 2 == 0:
                            if self.x < WIDTH - 20:
                                self.x += BODY // log.speed
                        else:
                            if self.x > 20:
                                self.x -= BODY // log.speed
                            
class Car:
    """ A vehicle that can run over the player in the street area. """
    def __init__(self, y, color, number, speed):
        self.y = y
        self.color = color
        self.number = number
        self.speed = speed
        self.spawn_car = False
        if self.number % 2 == 0:
            self.left = True
            self.x = 0
        else:
            self.left = False
            self.x = WIDTH
    
    def draw_car(self, canvas):
        canvas.draw_line([self.x - BODY, self.y],[self.x + BODY, self.y], 
                         BODY, self.color)
    
    def update_car(self, move_left):
        if move_left:
            self.x += BODY // self.speed
        else:
            self.x -= BODY // self.speed
        
        if self.x < 0 or self.x > WIDTH:
            cars[self.number].remove(self)
            cars[self.number].append(Car(self.y, get_random_color(), 
                                    self.number, get_random_speed()))
    def spawn_new_car(self):
        if len(cars[self.number]) < 2:
            if self.speed == 6:
                cars[self.number].append(Car(self.y, get_random_color(),
                                        self.number, 6))
            else:
                cars[self.number].append(Car(self.y, get_random_color(),
                                            self.number, random.randrange(self.speed, 6)))
                
class Log(Car):
    """ Objects for the player to hop on when they reach the river. """
    def __init__(self, y, number, speed):
        self.y = y
        self.number = number
        self.speed = speed
        self.spawn_log = False
        self.has_frog = False
        r = random.randrange(3)
        if r < 2:
            self.color = "Brown"
        else:
            self.color = "Green"
        if self.number % 2 == 0:
            self.x = 0
            self.left = True
        else:
            self.x = WIDTH
            self.left = False
            
    def update_log(self, move_left):
        if move_left:
            self.x += BODY // self.speed
        else:
            self.x -= BODY // self.speed
        
        if self.x < 0 or self.x > WIDTH:
            logs[self.number].remove(self)
            logs[self.number].append(Log(self.y, self.number, get_random_speed() + 3))
            
    def spawn_new_log(self):
        if len(logs[self.number]) < 3:
            if self.speed == 9:
                logs[self.number].append(Log(self.y, self.number, 9))
            else:
                logs[self.number].append(Log(self.y, self.number, 
                                             random.randrange(self.speed, 9)))

def start_game():
    global frog, cars, logs
    frog = Frog()
    cars = []
    logs = []
        
    for i in range(8):
        cars.append(
            [Car((i * BODY * 2) + 16 * BODY, 
            get_random_color(), i, get_random_speed())]
            )
    for j in range(4):
        logs.append(
            [Log((j * BODY * 2) + 4 * BODY, j, get_random_speed() + 3)]
            )
        
def get_random_color():
    return colors[random.randrange(6)]

def get_random_speed():
    return random.randrange(2, 6)
    
def keydown(key):
    global frog
    keys = simplegui.KEY_MAP
    
    if key == keys["left"]:
        if frog.x > 20:
            frog.x -= WIDTH // (BODY * 3)
    elif key == keys["right"]:
        if frog.x < WIDTH - 20:
            frog.x += WIDTH // (BODY * 3)
    elif key == keys["up"]:
        if frog.y > 25:
            frog.y -= WIDTH // 24
    elif key == keys["down"]:
        if frog.y < HEIGHT - BODY:
            frog.y +=  WIDTH // 24
    
def keyup(key):
    global frog

def draw(canvas):
    global cars, logs
    
    # draw background
    canvas.draw_line([0, BODY * 6], [WIDTH, BODY * 6], 
                     BODY * 9, "Blue")
    canvas.draw_line([0, BODY], [WIDTH, BODY], 
                     BODY * 2.5, "Green")
    canvas.draw_line([0, BODY * 11.5], [WIDTH, BODY * 11.5], 
                     BODY * 2,"Green")
    canvas.draw_line([0, BODY * 13.5], [WIDTH, BODY * 13.5], 
                     BODY * 2 + 2, "Gray")
    canvas.draw_line([0, HEIGHT - BODY], [WIDTH, HEIGHT - BODY], 
                     BODY * 2, "Gray")
    
    # draw street
    for y in range(20 * BODY, HEIGHT - (BODY * 2), BODY * 4):
        for x in range(BODY // 2, WIDTH, BODY * 2):
            canvas.draw_line([x, y - BODY], [x + BODY, y - BODY], 
                            4, "White")
    
    # draw logs
    for path in logs:
        for log in path:
            log.draw_car(canvas)
            log.update_log(log.left)
            
            if not log.spawn_log and (log.x == WIDTH // 4 or log.x == (3 * WIDTH) // 4):
                log.spawn_log = True
                log.spawn_new_log()
    
    # draw frog
    frog.draw_frog(canvas)
    
    # draw cars
    for street in cars:
        for car in street:
            car.draw_car(canvas)
            car.update_car(car.left)
            
            if not car.spawn_car and (car.x == WIDTH // 4 or car.x == (3 * WIDTH) // 4):
                car.spawn_car = True
                car.spawn_new_car()
    
    # check for collision with car
    frog.collide_with_car()
    
    # check if sitting on log
    frog.sitting_on_log()
    
    # check if frog is at the river and not on any log
    at_river = frog.y - BODY < logs[-1][0].y
    on_log = False
    for path in logs:
        for log in path:
            if log.has_frog:
                on_log = True
    if at_river and not on_log:
        start_game()

frame = simplegui.create_frame("frog", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

frame.start()
start_game()