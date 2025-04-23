import sys
import math
import stdio, stdarray, stdrandom, stddraw, stdaudio  # type: ignore
import game-objects.enemies as en
import game-objects.missiles as ms
from game-objects.shooter import Shooter
import game-objects.gamewindow as gw
import game-objects.env
import titlesc as tit

def main() -> None:  # Need the return type for mypy to type-check the body

    #title screen
    tit.showtitle_sc()
    shooter = Shooter(...)
    enemies = []
    en_missiles = []
    missiles = []
    lvl_num = 1
    while True:
        enemies = en.load_level(lvl_num)
        while len(enemies) != 0:
            v_x = animate_form(enemies)
            shooter.update_pos()
            for i in len(missiles):
                missiles[i].update()
            for i in len(en_missiles):
                en_missiles[i].update()
            ms.detect_collisions(missiles, enemies)
            ms.player_damage(en_missiles, shooter)
            en.over_check()
            gw.show_window()
        lvl_num += 1


if __name__ == "__main__":
    main()
