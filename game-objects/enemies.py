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
            stddraw.picture(self.image, self.x, self.y, 0.4, 0.4)

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

def create_enemies(rows: int, cols: int, distance, x_pos: float, y_pos: float, e_pic: str) -> list[list[float]]:
    
    pic = e_pic
    d = distance
    enemies = stdarray.create2D(rows, cols, None) 
    #intialized all enemies to zero, but could've just put (None)
    for i in range(rows):
        for j in range(cols):
            x = -x_pos + j*d
            y = y_pos - i*d
            enemies[i][j] = Enemy(x,y,pic)
    return enemies

def animate_enemies(enemies, rows: int, cols: int, vx: float, vy: float): #Make so that all enemies get animated at the same time

    
    #checks if edge has been reached on each enemy
    for i in range(rows):
        for j in range(cols):
            enemy = enemies[i][j]
                
            #condition that checks if wall reached
            if abs(enemy.x + vx) + RADIUS > 3.0:
                    
                #changes the horizontal direction when edge reached
                vx = -vx
                
                #moves all enemies one down if edge reached
                for n in range(rows):
                    for m in range(cols):
                        enemies[n][m].move(0,vy)

                #play sound
                enemy.wall_hit(12, 0.07)

    #moves all the enemies horizontally based on direction in (vx)
    for i in range(rows):
        for j in range(cols):
            enemies[i][j].move(vx, 0)

    #draws all the enemies according to the formating in class Enemy
    for i in range(rows):
        for j in range(cols):
            enemies[i][j].draw()

    return vx


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
    
    d = 0.45

    enemies_1 = create_enemies(rows_1, cols_1, d, 0.8, 1.6, "enemy.jpg")
    enemies_2 = create_enemies(rows_2, cols_2, d, 0.8, 0.8, "enemy2.jpg")
    enemies_3 = create_enemies(rows_3, cols_3, d, 0.8, 0.0, "enemy3.jpg")
 

    missiles = stdarray.create1D(0, None)
    #missiles.append(missile(0.0, -1.5))
    
    stddraw.setPenColor(stddraw.WHITE)

    vx_1 = 0.025
    vy_1 = -0.10
    vx_2 = 0.025
    vy_2 = -0.10
    vx_3 = 0.025
    vy_3 = -0.10


    mvy = 0.10
    p = 0
    pint = 30
    #n = 0

#    explosion = playnotes.explosion(0.5)
        
    while True:
        
        stddraw.clear(stddraw.BLACK)

        #Used a function to create the enemies
        #have to say vx equals the function so vx can be updated and the proper direction can be maintained
        vx_1 = animate_enemies(enemies_1, rows_1, cols_1, vx_1, vy_1)
        vx_2 = animate_enemies(enemies_2, rows_2, cols_2, vx_2, vy_2)
        vx_3 = animate_enemies(enemies_3, rows_3, cols_3, vx_3, vy_3)


        if (p % pint == 0):
            missiles.append(missile(0.0, -2.5))

        for mis in missiles:
            if mis.alive:
                mis.move(mvy)
                mis.draw()

        check_hits(missiles, enemies_1)
        check_hits(missiles, enemies_2)
        check_hits(missiles, enemies_3)

        stddraw.show(DT)
        
        p += 1 

if __name__ == "__main__":
    main()
