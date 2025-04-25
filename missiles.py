import sys
import math
import stdio, stdrandom, stddraw, stdaudio, stdarray
import env
import enemies as en
import gamewindow as gw
import constants as cons
import threading
import shooter as sh
from picture import Picture

# X_MIN, X_MAX, Y_MIN, Y_MAX, FPS -> gamewindow.py

# constants
MISSILE_SIZE = 0.1
MISSILE_COLOR = stddraw.RED
MISSILE_VELOCITY = 4.5 # this can be experimented with (in units/s)
PI = math.pi
ENEMY_POINT_VALUE = 10

class Missile:

    x : float
    y : float
    ang : float # measured from vert, right is +

    def __init__(self, pos_x, pos_y, ang):
        self.x = pos_x
        self.y = pos_y
        self.ang = ang
        self.pic = Picture("missile.jpg")

    def update_pos(self): # FPS is a constant stored somewhere idk (maybe in some module to manage the game window)
        self.x += MISSILE_VELOCITY * math.sin(self.ang) / gw.FPS
        self.y += MISSILE_VELOCITY * math.cos(self.ang) / gw.FPS

    def draw_missile(self):
        stddraw.picture(self.pic, self.x, self.y, MISSILE_SIZE * 2, MISSILE_SIZE * 2)


#def detect_collision(missiles, enemies, shooter): # destroys missiles and enemies in collisions, as well as out of bounds missiles
#    for i in range(len(missiles)):
#        if missiles[i].x < gw.X_MIN or missiles[i].x > gw.X_MAX or missiles[i].y < gw.Y_MIN or missiles[i].y > gw.Y_MAX:
#            missiles.pop(i) 
#        else:
#            for k in range(env.BUNKER_NR):
#                if gw.X_MIN + (env.BUNKER_WIDTH * (2 * k + 1)) < missiles[i].x < gw.X_MIN + (env.BUNKER_WIDTH * (2 * (k + 1))) and gw.Y_MIN + env.BUNKER_DIST < missiles[i].y < gw.Y_MIN + env.BUNKER_DIST + env.BUNKER_THICKNESS:
#                    missiles.pop(i)
#                    break
#            for k in range(len(enemies)):
#                if math.sqrt((missiles[i].x - enemies[k].x) ** 2 + (missiles[i].y - enemies[k].y) ** 2) < cons.ENEMY_SIZE / 2:
#                    if enemies[k].pic == "mystery.png":
#                        if shooter.health < 3:
#                            shooter.health += 1
#                    missiles.pop(i)
#                    enemies.pop(k)
#                    gw.add_points(ENEMY_POINT_VALUE)
#                    break

def detect_collision(missiles, enemies, shooter):
    i = 0
    while i < (len(missiles)) and i >= 0:
        if missiles[i].x < gw.X_MIN or missiles[i].x > gw.X_MAX or missiles[i].y < gw.Y_MIN or missiles[i].y > gw.Y_MAX:
            missiles.pop(i)
            i -= 1
        else:
            for k in range(env.BUNKER_NR):
                flag = False
                if gw.X_MIN + (env.BUNKER_WIDTH * (2 * k + 1)) < missiles[i].x < gw.X_MIN + (env.BUNKER_WIDTH * (2 * (k + 1))) and gw.Y_MIN + env.BUNKER_DIST < missiles[i].y < gw.Y_MIN + env.BUNKER_DIST + env.BUNKER_THICKNESS:
                    missiles.pop(i)
                    i -= 1
                    flag = True
                    break
            if flag:
                continue
            k = 0
            while k < len(enemies) and k >= 0:
                
                if isinstance(enemies[k], en.Boss):
                    collision_size = cons.BOSS_SIZE
                else:
                    collision_size = cons.ENEMY_SIZE

                if math.sqrt((missiles[i].x - enemies[k].x) ** 2 + (missiles[i].y - enemies[k].y) ** 2) < collision_size / 2:
                    threading.Thread(target=stdaudio.playFile, args=("explosion",)).start()
                    if enemies[k].pic == "mystery.png":
                        if shooter.health < 3:
                            shooter.health += 1
                    missiles.pop(i)
                    if isinstance(enemies[k], en.Boss):
                        enemies[k].health -= 1
                        if enemies[k].health == 0:
                            enemies.pop(k)
                    else:
                        enemies.pop(k)
                    k -= 1
                    i -= 1
                    gw.add_points(ENEMY_POINT_VALUE)
                    break
                k += 1
            
        i += 1

def player_damage(missiles, shooter):
    i = 0
    while i < (len(missiles)) and i >= 0:
        if missiles[i].x < gw.X_MIN or missiles[i].x > gw.X_MAX or missiles[i].y < gw.Y_MIN or missiles[i].y > gw.Y_MAX:
            missiles.pop(i)
            i -= 1
        else:
            for k in range(env.BUNKER_NR):
                flag = False
                if gw.X_MIN + (env.BUNKER_WIDTH * (2 * k + 1)) < missiles[i].x < gw.X_MIN + (env.BUNKER_WIDTH * (2 * (k + 1))) and gw.Y_MIN + env.BUNKER_DIST < missiles[i].y < gw.Y_MIN + env.BUNKER_DIST + env.BUNKER_THICKNESS:
                    missiles.pop(i)
                    i -= 1
                    flag = True
                    break
            if flag:
                continue
            if math.sqrt((missiles[i].x - shooter.x) ** 2 + (missiles[i].y - cons.SHOOTER_DIST) ** 2) <= cons.SHOOTER_SIZE:
                threading.Thread(target=stdaudio.playFile, args=("explosion",)).start()
                missiles.pop(i)
                shooter.damage()
                i -= 1
                break
        i += 1
# TODO: make module tests

def main():
    pass

if __name__ == "__main__":
    main()
