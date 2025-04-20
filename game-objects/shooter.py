import sys
import math
import stdio, stdarray, stdrandom, stddraw, stdaudio  # type: ignore
import gamewindow as gw

# X_MIN, X_MAX, Y_MIN, Y_MAX, FPS -> gamewindow.py

# constants
SHOOTER_SIZE = 0.1
SHOOTER_DIST = 0.1
SHOOTER_SPEED = 3
SHOOTER_COLOR = stddraw.BLUE

class SHOOTER:
    x : float
    y : float
    
    def shooter_motion(self, pos_x, pos_y):
        self.x = pos_x
        self.y = pos_y

        # Boundary conditions
        pos_x = max(SHOOTER_SIZE/2,min(gw.X_MAX - SHOOTER_SIZE/2, pos_x))
        pos_y = max(SHOOTER_SIZE/2,min(gw.Y_MAX - SHOOTER_SIZE/2, pos_y))
    
    def move_shooter(self, pos_x, pos_y):
        self.x = pos_x
        self.y = pos_y
        
        keys = stddraw.getKeysPressed()
        if keys[stddraw.K_LEFT]:
            pos_x -= SHOOTER_SPEED
        if keys[stddraw.K_RIGHT]:
            pos_x += SHOOTER_SPEED
        if keys[stddraw.K_DOWN]:
            pos_y -= SHOOTER_SPEED
        if keys[stddraw.K_UP]:
            pos_y += SHOOTER_SPEED
        if keys[stddraw.K_q]:
            break
        
    def draw_shooter(self):
        stddraw.setPenColor(SHOOTER_COLOR)
        stddraw.filledSquare(self.x,self.y, SHOOTER_SIZE/2)
        

        

def main() -> None:  # Need the return type for mypy to type-check the body



if __name__ == "__main__":
    main()
