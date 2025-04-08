import stddraw
import shooter
import gamewindow as gw

BUNKER_NR = 3
BUNKER_THICKNESS = 0.1
BUNKER_DIST_SHTR = 0.15
BUNKER_DIST = shooter.SHOOTER_DIST + shooter.SHOOTER_SIZE + BUNKER_DIST_SHTR
BUNKER_WIDTH = (gw.X_MAX - gw.X_MIN) / (2 * BUNKER_NR + 1)

def draw_bunkers(): # if shooter behind bunker, disable shooting
    stddraw.setPenColor(stddraw.BLACK)
    for i in range(BUNKER_NR):
        stddraw.filledRectangle(gw.X_MIN + BUNKER_WIDTH * (2 * i + 1), gw.Y_MIN + BUNKER_DIST, BUNKER_WIDTH, BUNKER_THICKNESS)

def main():
    gw.init()
    draw_bunkers()
    gw.show_window()

if __name__ == "__main__":
    main()
