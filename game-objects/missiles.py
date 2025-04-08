import sys
import math
import stdio, stdrandom, stddraw, stdaudio, stdarray
import gamewindow, env, shooter
import enemies as en

# X_MIN, X_MAX, Y_MIN, Y_MAX, FPS -> gamewindow.py

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
        self.x += MISSILE_VELOCITY * math.sin(self.ang) / gamewindow.FPS
        self.y += MISSILE_VELOCITY * math.cos(self.ang) / gamewindow.FPS

    def draw_missile(self):
        stddraw.setPenColor(MISSILE_COLOR)
        stddraw.filledCircle(self.x, self.y, MISSILE_SIZE)


def detect_collision(missiles, enemies): # destroys missiles and enemies in collisions, as well as out of bounds missiles
    for i in range(len(missiles)):
        if missiles[i].x < X_MIN or missiles[i].x > X_MAX or missiles[i].y < Y_MIN or missiles[i].y > Y_MAX:
            missiles.pop(i) 
        else:
            for k in range(env.BUNKER_NR):
                if X_MIN + (BUNKERWIDTH * (2 * k + 1)) < missiles[i].x < X_MIN + (BUNKERWIDTH * (2 * (k + 1))) and Y_MIN + BUNKER_DIST < missiles[i].y < Y_MIN + BUNKER_DIST + BUNKER_THICKNESS:
                    missiles.pop[i]
                    break
            for k in range(len(enemies)):
                if (enemies[k].x - (en.ENEMY_SIZE / 2) < missiles[i].x < enemies[k].x + (en.ENEMY_SIZE / 2)) and (enemies[k].y - (en.ENEMY_SIZE / 2) < missiles[i].y < enemies[k].y + (en.ENEMY_SIZE / 2)):
                    enemies.pop(k)
                    missiles.pop(i)
                    break
    
# TODO: make module tests

def main():
    pass

if __name__ == "__name__":
    main()
