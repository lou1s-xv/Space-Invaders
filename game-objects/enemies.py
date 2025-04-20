import sys
import math
import stdio, stdarray, stdrandom, stddraw, stdaudio  # type: ignore
import gamewindow as gw
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


def create_form1(rows: int, cols: int, distance, x_start: float, y_start: float, e_pic1: str, e_pic2: str, e_pic3: str) -> list[Enemy]:
    
    #creating a infantry ranks formation
    d = distance
    enemies: list[Enemy] = [] 
    #intialized all enemies to (None)
    #Top rank
    for i in range(rows):
        for j in range(cols):
            x = x_start + j*d
            y = y_start - i*d
            enemies.append(Enemy(x,y,e_pic1))
    #middle rank
    for i in range(rows):
        for j in range(cols):
            x = x_start + j*d
            y = (y_start - 1.5) - i*d
            enemies.append(Enemy(x,y,e_pic2))
    #bottom rank
    for i in range(rows):
        for j in range(cols):
            x = x_start + j*d
            y = (y_start - 3.0) - i*d
            enemies.append(Enemy(x,y,e_pic3))


    return enemies

def create_form2(rows: int, cols: int, x_start: float, y_start: float, spacing: float, e_pic: str)-> list[Enemy]:
    
    #creating a pyramid formation
    d = spacing
    enemies: list[Enemy] = [] 
    
    
    for i in range(rows):
        en_row = cols - (2 * i)
        if (en_row <= 0):
            break
        start_x = x_start + ((cols - en_row) / 2) * d

        for j in range(en_row):
            x = start_x + j * d
            y = y_start - i * d
            print(f"Enemy at row {i}, index {j}, pos ({x:.2f}, {y:.2f})")             
            enemies.append(Enemy(x, y, e_pic))
    
    return enemies

def create_form3(pattern: list[int], x_cen: float, y_start: float, spacing: float, e_pic: str)-> list[Enemy]:

    #creating a diamond formation
    enemies: list[Enemy] = []
    
    #top grouping
    for i, count in enumerate(pattern):
        total_width = (count - 1) * spacing
        start_x = x_cen - total_width / 2
        y = y_start - i * spacing

        for j in range(count):
            x = start_x + j * spacing
            enemies.append(Enemy(x, y, e_pic))
    
    #middle right group
    for i, count in enumerate(pattern):
        total_width = (count - 1) * spacing
        start_x = (x_cen + 2) - total_width / 2
        y = (y_start - 2) - i * spacing

        for j in range(count):
            x = start_x + j * spacing
            enemies.append(Enemy(x, y, e_pic))

    #middle left grouping
    for i, count in enumerate(pattern):
        total_width = (count - 1) * spacing
        start_x = (x_cen - 2) - total_width / 2
        y = (y_start - 2) - i * spacing

        for j in range(count):
            x = start_x + j * spacing
            enemies.append(Enemy(x, y, e_pic))

    #bottom grouping
    for i, count in enumerate(pattern):
        total_width = (count - 1) * spacing
        start_x = x_cen - total_width / 2
        y = (y_start - 4) - i * spacing

        for j in range(count):
            x = start_x + j * spacing
            enemies.append(Enemy(x, y, e_pic))
   

    return enemies 

def create_form4(rows: int, cols: int, x_start: float, y_start: float, e_pic: str)-> list[Enemy]:

    #checkerboard pattern
    enemies = []
    d = 0.55
    
    for i in range(rows):
        for j in range(cols):
            x = x_start + j*d
            y = y_start - i*d
            if (i + j) % 2 == 0:
                enemies.append(Enemy(x,y,e_pic))
    
    return enemies

def create_mystery(x_pos: float, y_pos: float, pik: str):
    blitzer = Enemy(x_pos, y_pos, pik)
    return blitzer

def animate_mystery(mystery: Enemy, vx: float):
    
    #Draws and moves the mystery enemy 
    mystery.move(vx, 0)
    mystery.draw()

def animate_forms(enemies, vx: float, vy: float, running: bool):

    margin = cons.w/2

    hit_wall = False

    for enemy in enemies:
        if (enemy.x + margin) > gw.X_MAX or (enemy.x - margin) < gw.X_MIN:
            hit_wall = True
            break

    for enemy in enemies:
        if (enemy.y - margin) < gw.Y_MIN:
            running[0] = False

    if hit_wall:
        
        vx = -vx

        for enemy in enemies:
            enemy.move(0, vy)
        enemies[0].wall_hit()

    for enemy in enemies:
        enemy.move(vx, 0)

    for enemy in enemies:
        enemy.draw()

    return vx


def game_over():
    stddraw.clear(stddraw.BLACK)
    stddraw.setPenColor(stddraw.WHITE)
    stddraw.setFontSize(50)
    stddraw.text(5, 5, "GAME OVER")
    stddraw.show()
    stddraw.pause(10000)


def main() -> None:  # Need the return type for mypy to type-check the body

    stddraw.setXscale(gw.X_MIN, gw.X_MAX)
    stddraw.setYscale(gw.Y_MIN, gw.Y_MAX)

    stddraw.clear(stddraw.BLACK)
    
    #Creating the various enemies
    mystery = create_mystery(9, 9, "mystery.png")
    #enemies1 = create_form1(cons.l1_rows, cons.l2_cols, cons.l1_spacing, cons.l1_xstart, cons.l1_ystart, "enemy.png", "enemy2.png", "enemy3.png")
    #enemies2 = create_form2(cons.l2_rows, cons.l2_cols, cons.l2_xstart, cons.l2_ystart, cons.l2_spacing, "enemypym.png")
    enemies3 = create_form3(cons.l3_pattern, cons.l3_xcen, cons.l3_ystart, cons.l3_spacing, "enemydiamond.png")
    #enemies4 = create_form4(cons.l4_rows, cons.l4_cols, cons.l4_xstart, cons.l4_ystart, "enemypym.png")

    stddraw.setPenColor(stddraw.WHITE)
    
    #vx has to be defined in main in order for the direction to be updated
    vx = cons.gen_vx
    
    #Game over check variable
    running: list[bool] = [True]

    while running[0]:

             
        stddraw.clear(stddraw.BLACK)
        
        #Used a function to create the enemies
        #have to say vx equals the function so vx can be updated and the proper direction can be maintained
        
        #vx = animate_form2(enemies, vx, cons.gen_vy, running)
        
        vx = animate_forms(enemies3, vx, cons.gen_vy, running)
        
        animate_mystery(mystery, cons.mvx)
            
        stddraw.show(cons.DT)
        
    game_over()

if __name__ == "__main__":
    main()
