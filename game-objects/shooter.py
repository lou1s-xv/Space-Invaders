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

# initial position
pos_x = gw.X_MAX/2
pos_y = 0.1

class SHOOTER:
    x : float
    y : float
    
    def shooter_motion(self, pos_x, pos_y):
        self.x = pos_x
        self.y = pos_y
        
        image_path = Picture('shooter.JPG')

        # main loop
        while True:
            stddraw.clear()
            stddraw.picture(image_path,pos_x,pos_y) 
            
            if stddraw.hasNextKeyTyped():
                key = stddraw.nextKeyTyped()
                if key == stddraw.KEYUP:
                    pos_y += SHOOTER_SPEED
                elif key == stddraw.KEYDOWN:
                    pos_y -= SHOOTER_SPEED
                elif key == stddraw.K_LEFT:
                    pos_x -= SHOOTER_SPEED
                elif key == stddraw.K_RIGHT:
                    pos_x += SHOOTER_SPEED
                elif key == stddraw.K_ESCAPE:
                    break
                    
            # Boundary conditions
            pos_x = max(SHOOTER_SIZE/2,min(gw.X_MAX - SHOOTER_SIZE/2, pos_x))
            pos_y = max(SHOOTER_SIZE/2,min(gw.Y_MAX - SHOOTER_SIZE/2, pos_y))
            
            stddraw.show()
    
    
def main() -> None:  # Need the return type for mypy to type-check the body



if __name__ == "__main__":
    main()
