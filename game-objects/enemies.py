import sys
import math
import stdio, stdarray, stdrandom, stddraw, stdaudio  # type: ignore
from dataclasses import dataclass
import playnotes
import playthattune
from picture import Picture

RADIUS = 0.15
DT = 20.0

@dataclass
class Enemy:
    x: float
    y: float
    pic: str
    alive = True
    


    def __init__(self, x: float, y: float, pic:str):
        self.x = x
        self.y = y
        self.image = Picture(pic) 
    
    def move(self, dx, dy):
        if self.alive:
            self.x += dx
            self.y += dy

    def draw(self):
        if self.alive:
            stddraw.picture(self.image, self.x, self.y, 0.3, 0.3)

    def dead(self):
        self.alive = False

    def wall_hit(self, note:float, time: float):

        freq = 440 * 2**(note/12)
        final = playthattune.chord(freq, time)
        stdaudio.playSamples(final)

@dataclass
class missile:

    x:float
    y:float
    alive = True

    def dead(self):
        self.alive = False

    def move(self, dy):
        if self.y < 3.0:
            self.y += dy
        else:
            self.alive = False

    def draw(self):
        if self.alive:
            stddraw.filledCircle(self.x, self.y, 0.05)

def create_infantry(rows: int, cols: int, distance, x_pos: float, y_pos: float, e_pic: str) -> list[list[Enemy]]:
    
    d = distance
    enemies = stdarray.create2D(rows, cols, None) 
    #intialized all enemies to zero, but could've just put (None)
    for i in range(rows):
        for j in range(cols):
            x = -x_pos + j*d
            y = y_pos - i*d
            enemies[i][j] = Enemy(x,y,e_pic)
    return enemies

def create_mystery(x_pos: float, y_pos: float, pik: str):

    blitzer = Enemy(x_pos, y_pos, pik)

    return blitzer

def animate_enemies(enemies_1: Enemy,enemies_2: Enemy, enemies_3: Enemy, rows: int, cols: int, vx: float, vy: float): #Make so that all enemies get animated at the same time

    
    #checks if edge has been reached on each enemy
    for i in range(rows):
        for j in range(cols):
            enemy_1 = enemies_1[i][j]
            enemy_2 = enemies_2[i][j]
            enemy_3 = enemies_3[i][j]

            #condition that checks if wall reached
            if (abs(enemy_1.x + vx) + RADIUS > 3.0) or (abs(enemy_2.x + vx) + RADIUS > 3.0) or (abs(enemy_3.x + vx) + RADIUS > 3.0):
                    
                #changes the horizontal direction when edge reached
                vx = -vx
                
                #moves all enemies one down if edge reached
                for n in range(rows):
                    for m in range(cols):
                        enemies_1[n][m].move(0,vy)
                        enemies_2[n][m].move(0,vy)
                        enemies_3[n][m].move(0,vy)

                #play sound
                enemy_1.wall_hit(12, 0.07)
                enemy_2.wall_hit(12, 0.07)
                enemy_3.wall_hit(12, 0.07)

#            if (abs(enemy_1.y + vy) + RADIUS > 3.0) or (abs(enemy_2.y + vy) + RADIUS > 3.0) or (abs(enemy_3.y + vy) + RADIUS > 3.0):


    #moves all the enemies horizontally based on direction in (vx)
    for i in range(rows):
        for j in range(cols):
            enemies_1[i][j].move(vx, 0)
            enemies_2[i][j].move(vx, 0)
            enemies_3[i][j].move(vx, 0)

    #draws all the enemies according to the formating in class Enemy
    for i in range(rows):
        for j in range(cols):
            enemies_1[i][j].draw()
            enemies_2[i][j].draw()
            enemies_3[i][j].draw()

    return vx

def animate_mystery(mystery: Enemy, vx: float):

    if abs(mystery.x + vx) + RADIUS > 3.0:
        mystery.dead()

    mystery.move(vx, 0)
    mystery.draw()


def check_hit_mystery(missiles, mystery):
    for mis in missiles:
        if mis.alive:
            if mystery.alive and abs(mystery.x + mis.x) < 0.20 and abs(mystery.y + mis.y) < 0.20:
                mystery.dead()
                mis.dead()

def check_hits(missiles, enemies):
    for mis in missiles:
        if mis.alive:
            for row in enemies:
                for enemy in row:
                    if enemy.alive and abs(enemy.x - mis.x) < 0.20 and abs(enemy.y - mis.y) < 0.20:
                        enemy.dead()
                        mis.dead()
#                        stdaudio.playSamples(Explosion)

def main() -> None:  # Need the return type for mypy to type-check the body

    stddraw.setXscale(-3.0, 3.0)
    stddraw.setYscale(-3.0, 3.0)

    stddraw.clear(stddraw.BLACK)
    
    rows_1 = 2
    cols_1 = 8
    rows_2 = 2
    cols_2 = 8
    rows_3 = 2
    cols_3 = 8
    
    d = 0.35

    prize = create_mystery(2.8, 2.8, "enemy4.jpg")
    enemies_1 = create_infantry(rows_1, cols_1, d, 0.8, 1.6, "enemy.jpg")
    enemies_2 = create_infantry(rows_2, cols_2, d, 0.8, 0.8, "enemy2.jpg")
    enemies_3 = create_infantry(rows_3, cols_3, d, 0.8, 0.0, "enemy3.jpg")
 

    missiles = stdarray.create1D(0, None)
    #missiles.append(missile(0.0, -1.5))
    
    stddraw.setPenColor(stddraw.WHITE)

    vx = 0.025
    vy = -0.10
    pvx = -0.0125
    vx_2 = 0.025
    vy_2 = -0.10
    vx_3 = 0.025
    vy_3 = -0.10


    mvy = 0.10
    n = 0
    nint = 30
    #n = 0

#    explosion = playnotes.explosion(0.5)

        
    while True:

             
        stddraw.clear(stddraw.BLACK)
        
        stddraw.text(0, 2.8, "Hello")

        #Used a function to create the enemies
        #have to say vx equals the function so vx can be updated and the proper direction can be maintained
        vx = animate_enemies(enemies_1, enemies_2, enemies_3, rows_1, cols_1, vx, vy)
        
        animate_mystery(prize, pvx)

            
        if (n % nint == 0):
            missiles.append(missile(0.0, -2.5))

        for mis in missiles:
            if mis.alive:
                mis.move(mvy)
                mis.draw()

        check_hits(missiles, enemies_1)
        check_hits(missiles, enemies_2)
        check_hits(missiles, enemies_3)
        check_hit_mystery(missiles, prize)

        stddraw.show(DT)
        
#        p += 1 
        n += 1

if __name__ == "__main__":
    main()
