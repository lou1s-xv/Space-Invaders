import sys
import math
import stdio, stdarray, stdrandom, stddraw, stdaudio  # type: ignore
import gamewindow as gw

# X_MIN, X_MAX, Y_MIN, Y_MAX, FPS -> gamewindow.py

# constants
SHOOTER_SIZE = 0.1
SHOOTER_DIST = 0.1
SHOOTER_COLOR = stddraw.BLUE

class SHOOTER:
    x : float
    y : float
    
    def shooter_motion(self, pos_x,pos_y):
        self.x = pos_x
        self.y = pos_y
        
        self.x = gw.X_MAX//2 - SHOOTER_SIZE//2
        self.y = gw.Y_MAX - SHOOTER_SIZE - 1
    
    def mov_shooter(self,FPS):
        

def main() -> None:  # Need the return type for mypy to type-check the body

   
    
    
    
    

    stdio.writeln("hello world")


if __name__ == "__main__":
    main()
