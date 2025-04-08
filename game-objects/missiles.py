import sys
import math
import stdio, stdrandom, stddraw, stdaudio, stdarray
import gamewindow

# X_MIN, X_MAX, Y_MIN, Y_MAX, FPS -> gamewindow.py ???

# ENEMY_SIZE -> enemies.py ???

# constants
MISSILE_SIZE = 0.02
MISSILE_COLOR = stddraw.RED
MISSILE_VELOCITY = 1 # this can be experimented with (in units/s)
PI = math.pi

class Missile:

    x : float
    y : float
    ang : float # measured from vert, right is +

    def __init__(self, pos_x, pos_y, ang):
        self.x = pos_x
        self.y = pos_y
        self.ang = ang

    def update_pos(self, FPS): # FPS is a constant stored somewhere idk (maybe in some module to manage the game window)
        self.x += MISSILE_VELOCITY * math.sin(self.ang) / FPS
        self.y += MISSILE_VELOCITY * math.cos(self.ang) / FPS

    def draw_missile(self):
        stddraw.setPenColor(MISSILE_COLOR)
        stddraw.filledCircle(self.x, self.y, MISSILE_SIZE)


def detect_collision(missiles, enemies): # implemented in enemies or in missile?
    for i in range(len(missiles)):
        if missiles[i].x < X_MIN or missiles[i].x > X_MAX or missiles[i].y < Y_MIN or missiles[i].y > Y_MAX:
            missiles.pop(i)
        for k in range(len(enemies)):
            if (missiles[i].x in range(enemies[k].x - (ENEMY_SIZE / 2), enemies[k].x + (ENEMY_SIZE / 2))) and (missiles[i].y in range(enemies[k].y - (ENEMY_SIZE / 2), enemies[k].y + (ENEMY_SIZE / 2)))
                enemies.pop(k)
                missiles.pop(i)
    
# TODO: make module tests

def main():
    pass

if __name__ == "__name__":
    main()
