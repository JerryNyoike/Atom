import math

# screen size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# game states
MENU_STARTGAME = 0
MENU_ABOUT = 1
MENU_SCENE = 2
MENU_INGAME = 3
MENU_NEXTLEVEL = 4
MENU_GAMEOVER = 5
MENU_GAMEFINISH = 6

# player start
PLAYER_START_X = 40

# directions
DIR_UP = 0
DIR_DOWN = 1
DIR_LEFT = 2
DIR_RIGHT = 3

# physics constant
TOP_SPEED = 2
GRAVITY = 10
UP_FLY_SPEED = 3
DOWN_FLY_SPEED = GRAVITY
FORWARD_FLY_ACC = .18
BACKWARD_FLY_ACC = .09
FLY_START = 1
AIR_FRICTION = 0.3
ROTATE_ANGLE = 180
MAX_ANGLE = 15
ANGLE_SPEED = 300

class Physics:

    def current_direction(self, x, y):
        return math.cos(pos.x), math.sin(pos.y)

    def apply_forward_acceleration(self, x_vel, y_vel, x, y):
        x_vel += FORWARD_FLY_ACC * x + dt
        y_vel += FORWARD_FLY_ACC * y + dt

        # apply friction
        x_vel *= AIR_FRICTION
        y_vel *= AIR_FRICTION

        return x_vel, y_vel

    def apply_backward_acceleration(self, x_vel, y_vel, x, y):
        x_vel += BACKWARD_FLY_ACC * x + dt
        y_vel += BACKWARD_FLY_ACC * y + dt

        # apply friction
        x_vel *= AIR_FRICTION
        y_vel *= AIR_FRICTION

        return x_vel, y_vel


    
    

