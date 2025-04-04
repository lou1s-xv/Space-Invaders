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
        self.pic = pic
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
        if self.y < 2.0:
            self.y += dy
        else:
            self.alive = False

    def draw(self):
        if self.alive:
            stddraw.filledCircle(self.x, self.y, 0.05)

def create_enemies(rows: int, cols: int, distance, e_pic: str) -> list[list[float]]:
    
    pic = e_pic
    d = distance
    enemies = stdarray.create2D(rows, cols, None) 
    #intialized all enemies to zero, but could've just put (None)
    for i in range(rows):
        for j in range(cols):
            x = -0.8 + j*d
            y = 0.8 - i*d
            enemies[i][j] = Enemy(x,y,pic)
    return enemies

def animate_enemies(enemies, rows: int, cols: int, vx: float, vy: float):

    
    #checks if edge has been reached on each enemy
    for i in range(rows):
        for j in range(cols):
            enemy = enemies[i][j]
                
            #condition that checks if wall reached
            if abs(enemy.x + vx) + RADIUS > 2.0:
                    
                #changes the horizontal direction when edge reached
                vx = -vx
                
                #moves all enemies one down if edge reached
                for n in range(rows):
                    for m in range(cols):
                        enemies[n][m].move(0,vy)

                #play sound
                enemy.wall_hit(11, 0.1)

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
                    if enemy.alive and abs(enemy.x - mis.x) < 0.1 and abs(enemy.y - mis.y) < 0.1:
                        enemy.dead()
                        mis.dead()

def main() -> None:  # Need the return type for mypy to type-check the body

    stddraw.setXscale(-2.0, 2.0)
    stddraw.setYscale(-2.0, 2.0)

    stddraw.clear(stddraw.BLACK)
    
    rows = 4
    cols = 6
    d = 0.40

    enemies = create_enemies(rows, cols, d, "enemy.jpg")

    missiles = stdarray.create1D(0, None)
    #missiles.append(missile(0.0, -1.5))
    
    stddraw.setPenColor(stddraw.WHITE)

    vx = 0.015
    vy = -0.05
    mvy = 0.05
    p = 0
    pint = 30
    #n = 0
        
    while True:
        
        stddraw.clear(stddraw.BLACK)

        #Used a function to create the enemies
        #have to say vx equals the function so vx can be updated and the proper direction can be maintained
        vx = animate_enemies(enemies, rows, cols, vx, vy)
        
        if (p % pint == 0):
            missiles.append(missile(0.0, -1.5))

        for mis in missiles:
            if mis.alive:
                mis.move(mvy)
                mis.draw()

        check_hits(missiles, enemies)

        stddraw.show(DT)
        
        p += 1 

if __name__ == "__main__":
    main()
