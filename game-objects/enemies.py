import sys
import math
import stdio, stdarray, stdrandom, stddraw, stdaudio  # type: ignore
from dataclasses import dataclass

RADIUS = 0.10
DT = 20.0

@dataclass
class Enemy:
    x: float
    y: float

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def draw(self):
        stddraw.filledCircle(self.x, self.y, RADIUS)

def main() -> None:  # Need the return type for mypy to type-check the body

    stddraw.setXscale(-2.0, 2.0)
    stddraw.setYscale(-2.0, 2.0)

    stddraw.clear(stddraw.BLACK)
    
    rows = 6
    cols = 8
    d = 0.20

    enemies = stdarray.create2D(rows, cols, Enemy(0.0, 0.0)) #intialized all enemies to zero, but could've just put (None)
    for i in range(rows):
        for j in range(cols):
            x = -0.8 + j*d
            y = 0.8 - i*d
            enemies[i][j] = Enemy(x,y)
    
    stddraw.setPenColor(stddraw.WHITE)

    vx = 0.015
    vy = -0.05
        
    while True:
        
        stddraw.clear(stddraw.BLACK)
        #checks if edge has been reached on each enemy
        for i in range(rows):
            for j in range(cols):
                enemy = enemies[i][j]
            
                if abs(enemy.x + vx) + RADIUS > 2.0:
                    
                    #changes the horizontal direction when edge reached
                    vx = -vx
                
                    #moves all enemies one down if edge reached
                    for n in range(rows):
                        for m in range(cols):
                            enemies[n][m].move(0,vy)
        
        #moves all the enemies horizontally based on direction in (vx)
        for i in range(rows):
            for j in range(cols):
                enemies[i][j].move(vx, 0)

        for i in range(rows):
            for j in range(cols):
                enemies[i][j].draw()
        
        stddraw.show(DT)

if __name__ == "__main__":
    main()
