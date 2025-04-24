import gamewindow as gw
from game_state import GameState
from titlesc import showtitle_sc
import stddraw

def main() -> None:  # Need the return type for mypy to type-check the body

    gw.init()
    showtitle_sc()
    
    game = GameState()
    
    while True:
        gw.clear_window()
        
        if game.game_over:
            gw.game_over()
            stddraw.show(2000)
            game = GameState() # reinstantiates game state, showing title screen must form a part of the game state
            continue
            
        game.update()
        game.draw()
        
        gw.show_window()

if __name__ == "__main__":
    main()
