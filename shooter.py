import math
import stddraw
from picture import Picture
import constants as cons
import gamewindow as gw

class Shooter:
    def __init__(self, pos_x, pos_y, angle):
        self.x = pos_x
        self.y = pos_y
        self.angle = angle
        self.health = 3
        self.speed = cons.SHOOTER_SPEED
        #self.last_angle = None
        self.cooldown = 0
        self.moving_left = False
        self.moving_right = False
        self.rotating_left = False
        self.rotating_right = False
        self._original = Picture("shooter.jpg")
        self.rotated_cache = {}
        self._cache_angles()
    
    
    def _cache_angles(self):
        for deg in range(0, 360, 15):
            rad = math.radians(deg)
            self.rotated_cache[deg] = self._rotate_image(rad)
    
    #adapted tut3 code
    def _rotate_image(self, angle):
        theta = -angle
        w, h = self._original.width(), self._original.height()
        rotated = Picture(w, h)
        cx, cy = w // 2, h // 2

        for tx in range(0, w, 2):  # Optimization: skip every other pixel
            for ty in range(0, h, 2):
                dx, dy = tx - cx, ty - cy
                sx = int(dx * math.cos(theta) - dy * math.sin(theta) + cx)
                sy = int(dx * math.sin(theta) + dy * math.cos(theta) + cy)
                if 0 <= sx < w and 0 <= sy < h:
                    rotated.set(tx, ty, self._original.get(sx, sy))
        return rotated
        
    def update(self):
        # Handle continuous movement
        if self.moving_left:
            self.x -= self.speed / gw.FPS
        if self.moving_right:
            self.x += self.speed / gw.FPS
            
        # Handle continuous rotation
        if self.rotating_left:
            self.angle = min(math.pi, self.angle - cons.ANGLE_STEP)
        if self.rotating_right:
            self.angle = max(0, self.angle + cons.ANGLE_STEP)
        
        # Boundary checking
        self.x = max(gw.X_MIN + 0.5, min(gw.X_MAX - 0.5, self.x))
        
        # Cooldown timer
        if self.cooldown > 0:
            self.cooldown -= 1

    def draw(self):
        deg = round(math.degrees(self.angle) / 15) * 15
        image = self.rotated_cache.get(deg % 360, self._original)
        stddraw.picture(image, self.x, self.y, 1, 1)
    
    
def handle_input(shooter, missile_list):
    while stddraw.hasNextKeyTyped():
        key = stddraw.nextKeyTyped().lower()
        
        # Movement keys (toggle state)
        if key == 'a':
            shooter.moving_left = not shooter.moving_left
            shooter.moving_right = False
        elif key == 'd':
            shooter.moving_right = not shooter.moving_right
            shooter.moving_left = False
            
        # Rotation keys (toggle state)
        elif key == 'j':
            shooter.rotating_left = not shooter.rotating_left
            shooter.rotating_right = False
        elif key == 'l':
            shooter.rotating_right = not shooter.rotating_right
            shooter.rotating_left = False
        elif key == 's':
            shooter.moving_left = False
            shooter.moving_right = False
            shooter.rotating_left = False
            shooter.rotating_right = False
            
        # Shooting (instant action)
        elif key == ' ' and shooter.cooldown <= 0:
            from missiles import Missile
            missile_list.append(Missile(shooter.x, shooter.y + 0.02, shooter.angle))
            shooter.cooldown = 10  # Cooldown frames
            
        # Quit game
        elif key == 'q':
            import sys
            sys.exit()
    
def main():
    
    gw.init()
    
    shooter = Shooter(5, 1, math.pi/2)
    missile_list = []

    while True:
        gw.clear_window()

        

        gw.show_window()
      
if __name__ == "__main__":
    main()
