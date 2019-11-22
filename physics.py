import math

# physics constant
GRAVITY = 10
X_FLY_SPEED = 3
Y_FLY_SPEED = GRAVITY
FORWARD_FLY_ACC = .18
BACKWARD_FLY_ACC = .09
FLY_START = FLY_SPEED / 6
AIR_FRICTION = 0.3

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


    
    

