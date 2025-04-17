import sys
import math
import stdio, stdarray, stdrandom, stddraw, stdaudio  # type: ignore
from dataclasses import dataclass
import threading
from picture import Picture
import constants as cons


class Enemy:
    x: float
    y: float
    pic: str
    
    #intializing the position and picture to be used for enemy
    def __init__(self, x: float, y: float, pic:str):
        self.x = x
        self.y = y
        self.image = Picture(pic) 
    
    #Moves the enemy based on input
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    
    #Draws the enemy based on image
    def draw(self):
        stddraw.picture(self.image, self.x, self.y, cons.w, cons.h)
    
    #wall hit sound
    def wall_hit(self):
      threading.Thread(target=stdaudio.playFile, args=("beep",)).start()


def create_infantry(rows: int, cols: int, distance, x_pos: float, y_pos: float, e_pic: str) -> list[Enemy]:
    d = distance
    enemies = stdarray.create1D(rows * cols, None) 
    #intialized all enemies to (None)
    for i in range(rows):
        for j in range(cols):
            x = -x_pos + j*d
            y = y_pos - i*d
            enemies[i * cols + j] = Enemy(x,y,e_pic)
    return enemies

def create_mystery(x_pos: float, y_pos: float, pik: str):
    blitzer = Enemy(x_pos, y_pos, pik)
    return blitzer

def animate_enemies(enemies_1: Enemy,enemies_2: Enemy, enemies_3: Enemy, rows: int, cols: int, vx: float, vy: float, running: list): 
    #Made so that all enemies get animated at the same time
    #checks if edge has been reached on each enemy
    for i in range(rows):
        for j in range(cols):
            enemy_1 = enemies_1[i * cols + j]
            enemy_2 = enemies_2[i * cols + j]
            enemy_3 = enemies_3[i * cols + j]

            #condition that checks if wall reached
            if (abs(enemy_1.x + vx) + cons.RADIUS > 3.0) or (abs(enemy_2.x + vx) + cons.RADIUS > 3.0) or (abs(enemy_3.x + vx) + cons.RADIUS > 3.0):
                    
                #changes the horizontal direction when edge reached
                vx = -vx
                
                #moves all enemies one down if edge reached
                for n in range(rows):
                    for m in range(cols):
                        enemies_1[n * cols + m].move(0,vy)
                        enemies_2[n * cols + m].move(0,vy)
                        enemies_3[n * cols + m].move(0,vy)
                
                #play sound
                enemy_1.wall_hit()
            
            #checks if the bottom was reached
            if (abs(enemy_1.y + vy) + cons.RADIUS > 3.0) or (abs(enemy_2.y + vy) + cons.RADIUS > 3.0) or (abs(enemy_3.y + vy) + cons.RADIUS > 3.0):
                running[0] = False


    #moves all the enemies horizontally based on direction in (vx)
    for i in range(rows):
        for j in range(cols):
            enemies_1[i * cols + j].move(vx, 0)
            enemies_2[i * cols + j].move(vx, 0)
            enemies_3[i * cols + j].move(vx, 0)

    #draws all the enemies according to the formating in class Enemy
    for i in range(rows):
        for j in range(cols):
            enemies_1[i * cols + j].draw()
            enemies_2[i * cols + j].draw()
            enemies_3[i * cols + j].draw()
    #returns vx so the horizontal direction can be updated
    return vx

def animate_mystery(mystery: Enemy, vx: float):
    
    #Draws and moves the mystery enemy 
    mystery.move(vx, 0)
    mystery.draw()

def game_over():
    stddraw.clear(stddraw.BLACK)
    stddraw.setPenColor(stddraw.WHITE)
    stddraw.setFontSize(50)
    stddraw.text(0.0, 0.5, "GAME OVER")
    stddraw.show()
    stddraw.pause(10000)


def main() -> None:  # Need the return type for mypy to type-check the body

    stddraw.setXscale(-3.0, 3.0)
    stddraw.setYscale(-3.0, 3.0)

    stddraw.clear(stddraw.BLACK)
    
    #Creating the various enemies
    mystery = create_mystery(2.8, 2.8, "enemy4.jpg")
    enemies_1 = create_infantry(cons.inf_rows1, cons.inf_cols1, cons.inf_d, 0.8, 1.6, "enemy.jpg")
    enemies_2 = create_infantry(cons.inf_rows2, cons.inf_cols2, cons.inf_d, 0.8, 0.8, "enemy2.jpg")
    enemies_3 = create_infantry(cons.inf_rows3, cons.inf_cols3, cons.inf_d, 0.8, 0.0, "enemy3.jpg")
        
    stddraw.setPenColor(stddraw.WHITE)
    
    #vx has to be defined in main in order for the direction to be updated
    vx = cons.inf_vx
    
    #Game over check variable
    running: list[bool] = [True]

    while running[0]:

             
        stddraw.clear(stddraw.BLACK)
        
        #Used a function to create the enemies
        #have to say vx equals the function so vx can be updated and the proper direction can be maintained
        vx = animate_enemies(enemies_1, enemies_2, enemies_3, cons.inf_rows1, cons.inf_cols1, vx, cons.inf_vy, running)
        
        animate_mystery(mystery, cons.mvx)
            
        stddraw.show(cons.DT)
        
    game_over()

if __name__ == "__main__":
    main()
