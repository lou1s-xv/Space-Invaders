import math
import shooter
import missiles
import enemies as en
import gamewindow as gw
import constants as cons

class GameState:
    def __init__(self):
        self.shooter = shooter.Shooter(5, 1, 0)
        self.enemies = en.load_level(1)
        self.player_missiles = []
        self.enemy_missiles = []
        self.score = 0
        self.level = 1
        self.enemy_vx = cons.gen_vx
        self.game_over = False
        self.player_win = False
        
    def update(self):
        # Input handling
        shooter.handle_input(self.shooter, self.player_missiles)
        
        # Update positions
        self.shooter.update()
        for missile in self.player_missiles:
            missile.update_pos()
        if self.level >= 3:
            en.maybe_fire_missiles(self.enemies, self.enemy_missiles)
            for missile in self.enemy_missiles:
                missile.update_pos()
        self.enemy_vx = en.animate_forms(self.enemies, self.enemy_missiles, self.enemy_vx, cons.gen_vy) 
        
        # Collision detection
        missiles.detect_collision(self.player_missiles, self.enemies)
        missiles.player_damage(self.enemy_missiles, self.shooter)
               
        # Game state checks
        self.check_level_complete()
        self.check_game_over()
    
    def draw(self):
        self.shooter.draw()
        for missile in self.player_missiles:
            missile.draw_missile()
        for enemy in self.enemies:
            enemy.draw()
        #Heart display will go here
        gw.draw_score()
    
    def check_level_complete(self):
        if not self.enemies:
            self.level += 1
            self.enemies = en.load_level(self.level)#changes enemy formation for next level
            gw.show_loading_screen(self.level) #Display loading screen
    
    def check_game_over(self):
        if self.shooter.health <= 0 or en.over_check(self.enemies, self.shooter):
            self.game_over = True
            gw.GAME_END = True #ends game music
            #gameover screen (YOU LOSE DISPLAY) , self.handle_game_over()

    def check_player_win(self):
        if not self.enemies and (self.level > 5):
            self.player_win = True
            gw.GAME_END = True #ends game
            #gameoverscreen (YOU WIN DISPLAY), self.handle_game_over()
    
    def handle_game_over(self):
        gw.game_over(self)
        #Can take a GameState argument and display corresponding game over screen
        self.__init__()  # Reset game
