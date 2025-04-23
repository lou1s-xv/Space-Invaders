import sys
import math
import stdio, stdarray, stdrandom, stddraw, stdaudio  # type: ignore
import gamewindow as gw
from picture import Picture

SHOOTER_SIZE = 0.5
SHOOTER_SPEED = 0.2

AIM_ANGLE = math.pi / 2
ANGLE_STEP = math.pi / 90

LEFT = False
RIGHT = False

class Shooter:
    def __init__(self, pos_x, pos_y, shooter_angle):
        self.x = pos_x
        self.y = pos_y
        self.angle = shooter_angle
        self.health = 3
        self.image = Picture("shooter.jpg")
        self.speed = SHOOTER_SPEED

    def draw(self):
        # Draw the shooter image
        rotate_shooter(self, self.angle)
        stddraw.picture(self.image, self.x, self.y)

        # Draw lives
        # import pictures for hearts(drawn in gamewindow)
       

    def damage(self):
        self.health = self.health - 1
        if self.health == 0:
            gameover()
                
    def update_pos(self):
        if stddraw.hasNextKeyTyped():
            key = stddraw.nextKeyTyped()
            if key == stddraw.KEY_LEFT:
                shooter.x -= shooter.speed
            if key == stddraw.KEY_RIGHT:
                shooter.x += shooter.speed
        

def input():
        global LEFT, RIGHT
        if stddraw.hasNextKeyTyped():
            key = stddraw.nextKeyTyped()
            if key == 'a':
                LEFT = True
                RIGHT = False
            elif key == 'd':
                LEFT = False
                RIGHT = True
            elif key == 's':
                LEFT = False
                Right = False

def update_aim(shooter: Shooter):
    global AIM_ANGLE
    if LEFT:
        AIM_ANGLE += ANGLE_STEP
    elif RIGHT:
        AIM_ANLGE -= ANGLE_STEP

def shot_fired(shooter, missile_list):
    from missiles import Missile
    if stddraw.hasNextKeyTyped():
        key = stddraw.nextKeyTyped()
        if key == ' ':
            missile_list.append(Missile(shooter.x, (shooter.y+0.02), self.angle))
        
        # inclue aiming code (missiles)
        #space bar control shooting
        # zero degree is initial angle, bounded between -90 and 90
        # shooting be controlled by A and D.
        # function for rotating the shooter, and function for shooting.

def rotate_shooter(shooter: Shooter, angle_degrees: float) -> None:
    theta = angle_degrees * math.pi / 180.0
    w, h = shooter.image.width(), shooter.image.height()
    cx, cy = w // 2, h // 2
    cos_theta = math.cos(-theta)
    sin_theta = math.sin(-theta)
    rotated = Picture(w, h)

    for tx in range(w):
        for ty in range(h):
            dx, dy = tx - cx, ty - cy
            sx = int(dx * cos_theta - dy * sin_theta + cx)
            sy = int(dx * sin_theta + dy * cos_theta + cy)
            color = stddraw.BLACK
            if 0 <= sx < w and 0 <= sy < h:
                color = shooter.image.get(sx, sy)
            rotated.set(tx, ty, color)

    # Replace original image with rotated one
    shooter.image = rotated

def animate(shooter: Shooter, missile_list):

    input()                 # Set LEFT / RIGHT flags
    update_aim(shooter)     # Use those flags to adjust aim
    shooter.update_pos()
    shot_fired(shooter, missile_list)

    shooter.draw()
    for missile in missile_list:
        missile.move()
        missile.draw()


def main():
    pass
      
if __name__ == "__main__":
    main()
