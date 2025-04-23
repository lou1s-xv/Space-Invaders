import sys
import math
import stdio, stdarray, stdrandom, stddraw, stdaudio  # type: ignore
import gamewindow as gw
from picture import Picture
from missiles import Missile

SHOOTER_SIZE = 0.5
SHOOTER_SPEED = 0.2


class Shooter:
    def __init__(self, pos_x, pos_y, shooter_angle):
        self.x = pos_x
        self.y = pos_y
        self.theta = shooter_angle
        self.health = 3

    def draw(self):
        # Draw the shooter image
        image_path = 'shooter.JPG'  
        stddraw.picture(image_path, self.x, self.y)

        # Draw lives
        # import pictures for hearts(drawn in gamewindow)
        bar_x = 0.1
        bar_y = 0.02
        width = self.x - bar_x / 2
        height = self.y + self.size + 0.05


        # Health bar border
        stddraw.setPenColor(stddraw.BLACK)
        stddraw.rectangle(width, height, bar_x, bar_y)

    def damage(self):
        self.health = self.health - 1
            if self.health == 0:
                gameover()
                
    def update_pos(self,missiles):
        if stddraw.hasNextKeyTyped():
            key = stddraw.nextKeyTyped()
            if key == stddraw.KEY_LEFT:
                shooter.x -= shooter.speed
            if key == stddraw.KEY_RIGHT:
                shooter.x += shooter.speed
                
        self.draw()
            
         
         
                    
        # Boundary conditions
        shooter.x = max(shooter.size / 2, min(gw.X_MAX - shooter.size / 2, shooter.x))
        shooter.y = max(shooter.size / 2, min(gw.Y_MAX - shooter.size / 2, shooter.y))
        
        # inclue aiming code (missiles)
        #space bar control shooting
        # zero degree is initial angle, bounded between -90 and 90
        # shooting be controlled by A and D.
        # function for rotating the shooter, and function for shooting.


def main():
    pass
      
if __name__ == "__main__":
    main()
