import sys
import math
import stdio, stdarray, stdrandom, stddraw, stdaudio  # type: ignore
import gamewindow as gw

SHOOTER_SIZE = 0.5
SHOOTER_SPEED = 0.2

class Shooter:
    def __init__(self, pos_x, pos_y):
        self.x = pos_x
        self.y = pos_y
        self.size = SHOOTER_SIZE
        self.speed = SHOOTER_SPEED
        self.color = stddraw.RED
        self.health = 100

    def draw(self):
        # Draw the shooter image
        image_path = 'shooter.JPG'  
        stddraw.picture(image_path, self.x, self.y)

        # Draw Health bar
        bar_x = 0.1
        bar_y = 0.02
        width = self.x - bar_x / 2
        height = self.y + self.size + 0.05

        # Health Bar background

        stddraw.setPenColor(stddraw.BLUE)
        stddraw.filledRectangle(width, height, bar_x, bar_y)


        # Health color
        health_width = bar_x * (self.health / 100)  
        health_color = stddraw.GREEN

        if self.health < 50:
            health_color = stddraw.YELLOW
        if self.health < 20:
            health_color = stddraw.RED
        stddraw.setPenColor(health_color)
        stddraw.filledRectangle(width, height, health_width, bar_y)


        # Health bar border
        stddraw.setPenColor(stddraw.BLACK)
        stddraw.rectangle(width, height, bar_x, bar_y)

    def damage(self, damage):
        self.health = max(0, self.health - damage)
        if self.health == 0:
            stdio.writeln("Shooter is dead!")

def main():
    stddraw.clear()
    
    # Initialize shooter at the center bottom of the window
    shooter = Shooter(gw.X_MAX / 2, 0.1)

    # main loop
    while True:
        if stddraw.hasNextKeyTyped():
            key = stddraw.nextKeyTyped()
            if key == stddraw.KEY_UP:
                shooter.y += shooter.speed
            elif key == stddraw.KEY_DOWN:
                shooter.y -= shooter.speed
            elif key == stddraw.KEY_LEFT:
                shooter.x -= shooter.speed
            elif key == stddraw.KEY_RIGHT:
                shooter.x += shooter.speed
            elif key == 'd':
                shooter.damage(10)
            elif key == stddraw.K_ESCAPE:
                break
                    
        # Boundary conditions
        shooter.x = max(shooter.size / 2, min(gw.X_MAX - shooter.size / 2, shooter.x))
        shooter.y = max(shooter.size / 2, min(gw.Y_MAX - shooter.size / 2, shooter.y))

        shooter.draw()
        stddraw.show(20)

if __name__ == "__main__":
    main()
