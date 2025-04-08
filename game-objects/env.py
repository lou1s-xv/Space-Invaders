import stddraw
import shooter, gamewindow

BUNKER_NR = 3
BUNKER_THICKNESS = 0.1
BUNKER_DIST_SHTR = 0.15
BUNKER_DIST = SHOOTER_DIST + SHOOTER_SIZE + BUNKER_DIST_SHTR
BUNKER_WIDTH = (X_MAX - X_MIN) / BUNKER_NR

def draw_bunkers(): # if shooter behind bunker, disable shooting
    for i in range(BUNKER_NR):
        stddraw.filledRectangle(X_MIN + BUNKER_WIDTH * (2 * i + 1), Y_MIN + BUNKER_DIST, X_MIN + BUNKER_WIDTH, BUNKER_THICKNESS)
    
def main():
    pass

if __name__ == "__main__":
    main()
