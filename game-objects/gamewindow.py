import stddraw

X_MIN = 0
X_MAX = 10
Y_MIN = 0
Y_MAX = 10
FPS = 30
INIT = False

def show_window():
    if INIT == False:
        stddraw.setXscale(X_MIN, XMAX)
        stddraw.setYscale(Y_MIN, Y_MAX)
        INIT = True
    stddraw.show()

def main():
    pass

if __name__ == "__main__":
    main()
