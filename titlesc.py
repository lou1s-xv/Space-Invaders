import sys
import math
import stdio, stdarray, stdrandom, stddraw, stdaudio # type: ignore
from picture import Picture
import gameobjects.constants as cons
import gameobjects.gamewindow as gw
import threading
import time

music_thread = None

class ene:
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
    def draw(self, w, h):
        stddraw.picture(self.image, self.x, self.y, w, h)

    def draw_scaled(self, size, w, h):
        stddraw.setPenColor(stddraw.WHITE)
        stddraw.picture(self.image, self.x, self.y, w * (size * 2), h * (size*2))


#create backgroud enemies
def bgen(rows: int, cols: int, distance, x_pos: float, y_pos: float, e_pic: str) -> list[ene]:
    d = distance
    enemies = stdarray.create1D(rows * cols, None)
    #intialized all enemies to (None)
    for i in range(rows):
        for j in range(cols):
            x = x_pos + j*d
            y = y_pos - i*d
            enemies[i * cols + j] = ene(x,y,e_pic)
    return enemies

def mbgen(enemies, rows: int, cols: int, vx: float, vy: float):
    
    margin = cons.ENEMY_SIZE/2

    hit_wall = False

    #Made so that all enemies get animated at the same time
    #checks if edge has been reached on each enemy
    for enemy in enemies:
        
        #condition that checks if wall reached
        if (enemy.x + margin) > gw.X_MAX or (enemy.x - margin) < gw.X_MIN:
            hit_wall = True
            break
    
    if hit_wall:

        #changes the horizontal direction when edge reached
        vx = -vx

    #moves all the enemies horizontally based on direction in (vx)
    for enemy in enemies:
        enemy.move(vx, 0)
    
    #draws all the enemies according to the formating in class Enemy
    for enemy in enemies:
        enemy.draw(cons.tw, cons.th)
    
    #returns vx so the horizontal direction can be updated
    return vx

def zoomcen(enemies, rows, cols, step_size, sx, sy):
  
    global music_thread
    spacing = 0.55  # space between enemies
    targets = []

    # Assign each enemy its final target position
    for i in range(rows):
        for j in range(cols):
            tx = sx + j * spacing
            ty = sy - i * spacing
            targets.append((tx, ty))

    # Stage 1: Move each enemy to its target position
    for idx, enemy in enumerate(enemies):
        tx, ty = targets[idx]
        while abs(enemy.x - tx) > 0.01 or abs(enemy.y - ty) > 0.01:
            dx = tx - enemy.x
            dy = ty - enemy.y
            length = (dx**2 + dy**2)**0.5
            if length == 0:
                break
            enemy.move(step_size * dx / length, step_size * dy / length)

            stddraw.clear(stddraw.BLACK)
            for e in enemies:
                e.draw(cons.tw, cons.th)
            stddraw.show(0.025)

    # Enemies now at center — begin "marching forward"
    final_size = 0.9  # Final big size
    grow_steps = 50   # Smooth animation frames

    for size_step in range(grow_steps):
        stddraw.clear(stddraw.BLACK)
        scale = (size_step + 1) / grow_steps * final_size
        for enemy in enemies:
            enemy.draw_scaled(scale, cons.tw, cons.th)
        stddraw.show(10)
    stddraw.setFontSize(40)
    stddraw.text(5, 5, "loading level 1...")
    while music_thread.is_alive():
        stddraw.show(cons.DT)

def play_music():
    stdaudio.playFile("Survivor - Eye Of The Tiger")

def start_music():
    global music_thread
    music_thread = threading.Thread(target=play_music)
    music_thread.start()

def showtitle_sc():

    image4 = Picture("Portal.png")
    start_music()
    enemies1 = bgen(cons.l1_rows, cons.l1_cols, cons.l1_spacing, 5, 9, "gameobjects/enemy.png")
    vx = cons.t_vx
    showing_help = False

    stddraw.setPenColor(stddraw.WHITE)
    while True:
        
        stddraw.clear(stddraw.BLACK)
        stddraw.picture(image4, 4.5, 5, 15, 10)
        
        if showing_help:

            stddraw.clear(stddraw.BLACK)
            stddraw.setFontSize(20)
            stddraw.setPenColor(stddraw.WHITE)
            stddraw.text(5, 9, "HELP")
            stddraw.text(5, 7, "Use arrow keys to move.")
            stddraw.text(5, 6, "Space to shoot.")
            stddraw.text(5, 5, "Avoid getting hit!")
            stddraw.text(5, 4, "press 'w' and 'h' to aim")
            stddraw.text(5, 2, "Press H to return to the title screen.")
        
        else:

            vx = mbgen(enemies1, cons.l1_rows, cons.l1_cols, vx, 0)

            # Draw title text on top (unchanging)
            stddraw.picture(Picture("Title.png"), 5, 5, 3, 3)
            stddraw.setFontSize(20)
            stddraw.text(5, 2, "Press SPACE to start...")
            stddraw.text(5, 1.5, "Press H for Help")
        
        stddraw.show(100)

        if stddraw.hasNextKeyTyped():
            key = stddraw.nextKeyTyped()
            if key == 'h':
                showing_help = not showing_help
            elif key == ' ':
                break
    
    zoomcen(enemies1, cons.l1_rows, cons.l1_cols, 0.01, 5, 8)

    stddraw.clear(stddraw.BLACK)
    stddraw.show(cons.DT)

    

def main() -> None:  # Need the return type for mypy to type-check the body

    stddraw.setXscale(gw.X_MIN, gw.X_MAX)
    stddraw.setYscale(gw.Y_MIN, gw.Y_MAX)
    showtitle_sc() 

if __name__ == "__main__":
    main()
