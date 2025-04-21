import sys
import math
import stdio, stdrandom, stddraw, stdaudio, stdarray
import env, shooter
import enemies as en
import gamewindow as gw
import constants as con

# X_MIN, X_MAX, Y_MIN, Y_MAX, FPS -> gamewindow.py

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

    def update_pos(self): # FPS is a constant stored somewhere idk (maybe in some module to manage the game window)
        self.x += MISSILE_VELOCITY * math.sin(self.ang) / gw.FPS
        self.y += MISSILE_VELOCITY * math.cos(self.ang) / gw.FPS

    def draw_missile(self):
        stddraw.setPenColor(MISSILE_COLOR)
        stddraw.filledCircle(self.x, self.y, MISSILE_SIZE)


def detect_collision(missiles, enemies): # destroys missiles and enemies in collisions, as well as out of bounds missiles
    for i in range(len(missiles)):
        if missiles[i].x < gw.X_MIN or missiles[i].x > gw.X_MAX or missiles[i].y < gw.Y_MIN or missiles[i].y > gw.Y_MAX:
            missiles.pop(i) 
        else:
            for k in range(env.BUNKER_NR):
                if gw.X_MIN + (env.BUNKERWIDTH * (2 * k + 1)) < missiles[i].x < gw.X_MIN + (env.BUNKERWIDTH * (2 * (k + 1))) and gw.Y_MIN + env.BUNKER_DIST < missiles[i].y < gw.Y_MIN + env.BUNKER_DIST + env.BUNKER_THICKNESS:
                    missiles.pop[i]
                    break
            for k in range(len(enemies)):
                if math.sqrt((missiles[i].x - enemies[k].x) ** 2 + (missiles[i].y - enemies[k].y) ** 2) < con.ENEMEY_SIZE / 2:
                    enemies.pop(k)
                    missiles.pop(i)
                    stddraw.playFile("explosion.wav")
                    break

def player_damage(missiles, shooter):
    for i in range(len(missiles)):
        if missiles[i].x < gw.X_MIN or missiles[i].x > gw.X_MAX or missiles[i].y < gw.Y_MIN or missiles[i].y > gw.Y_MAX:
            missiles.pop(i) 
        else:
            for k in range(env.BUNKER_NR):
                if gw.X_MIN + (env.BUNKERWIDTH * (2 * k + 1)) < missiles[i].x < gw.X_MIN + (env.BUNKERWIDTH * (2 * (k + 1))) and gw.Y_MIN + env.BUNKER_DIST < missiles[i].y < gw.Y_MIN + env.BUNKER_DIST + env.BUNKER_THICKNESS:
                    missiles.pop[i]
                    break
            if math.sqrt((missiles[i].x - shooter.x) ** 2 + (missiles[i].y - shooter.SHOOTER_DIST) ** 2) <= shooter.SHOOTER_SIZE:
                missiles.pop(i)
                shooter.health -= 1
                stddraw.playFile("explosion.wav")
                break
# TODO: make module tests

def main():
    pass

if __name__ == "__name__":
    main()
