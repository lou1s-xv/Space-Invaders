import sys
import math
import stdio, stdarray, stdrandom, stddraw, stdaudio  # type: ignore
import gamewindow as gw

# X_MIN, X_MAX, Y_MIN, Y_MAX, FPS -> gamewindow.py

class Shooter:
    x : float
    y : float
    
    def initial(shooter, pos_x, pos_y):
        shooter.x = pos_x
        shooter.y = pos_y

        # initial position
        pos_x = gw.X_MAX/2
        pos_y = 0.1

        shooter.size = 0.5
        shooter.speed = 0.2
        shooter.color = stddraw.RED
        shooter.health = 100
        
    def draw(shooter):
        
        image_path = Picture('shooter.JPG')
        stddraw.picture(image_path,pos_x,pos_y) 

        # Draw Health bar

        bar_x = 0.1
        bar_y = 0.02
        width = shooter.x - bar_x/2
        height = shooter.y + shooter.size +0.05

        # Health Bar background
        stddraw.setPenColor.(stddraw.BLUE)
        stddraw.filledRectangle(width,height,bar_x,bar_y)

        # Health color
        health_width = bar_x * (shooter.health/50)
        health_color = stddraw.GREEN

        if shooter.health < 50:
            health_color = stddraw.YELLOW
        elif shooter.health < 20:
            health_color = stddraw.RED
            
        stddraw.setPenColor(health_Color)
        stddraw.filledRectangle(width,height,health_width,bar_y)

        # Health bar border
        stddraw.setPenColor(stddraw.BLACK)
        stddraw.rectangle(width,height,bar_x,bar_y)
    
    def damage(shooter, damage):
        shooter.health =max(0, shooter.health-damage)
        if shooter.health == 0:
            stdio.writeln("Shooter is dead!")

            
def main():

    stddraw.clear()
    
    # main loop
    while True:
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
            elif key == 'd':
                shooter.damage(10)
            elif key == stddraw.K_ESCAPE:
                break
                    
        # Boundary conditions
        pos_x = max(SHOOTER_SIZE/2,min(gw.X_MAX - SHOOTER_SIZE/2, pos_x))
        pos_y = max(SHOOTER_SIZE/2,min(gw.Y_MAX - SHOOTER_SIZE/2, pos_y))

        shooter.draw()
            
        stddraw.show(20)


if __name__ == "__main__":
    main()
