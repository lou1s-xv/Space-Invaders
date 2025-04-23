import sys
import math
import stdio, stdarray, stdrandom, stddraw, stdaudio  # type: ignore
import gameobjects.enemies as en
import gameobjects.missiles as ms
from gameobjects.shooter import Shooter
import gameobjects.gamewindow as gw
import gameobjects.env
import gameobjects.constants as cons
import titlesc as tit

def main() -> None:  # Need the return type for mypy to type-check the body

    #title screen
    tit.showtitle_sc()
    gw.play_game_music
    shooter = Shooter(...)
    enemies = []
    en_missiles = []
    missiles = []
    lvl_num = 1
    v_x = cons.gen_vx
    while True:
        enemies = en.load_level(lvl_num)
        while len(enemies) != 0:
            gw.clear_window()
            v_x = animate_form(enemies)
            shooter.update_pos(missiles)
            for mis in missiles:
                mis.update()
            for mis in en_missiles:
                mis.update()
            ms.detect_collisions(missiles, enemies)
            ms.player_damage(en_missiles, shooter)
            en.over_check(enemies, shooter)
            gw.show_window()
        lvl_num += 1


if __name__ == "__main__":
    main()
