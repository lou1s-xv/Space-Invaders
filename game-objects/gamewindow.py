import stddraw

X_MIN = 0
X_MAX = 10
Y_MIN = 0
Y_MAX = 10
FPS = 30
score = 0

def init():
    stddraw.setXscale(X_MIN, X_MAX)
    stddraw.setYscale(Y_MIN, Y_MAX)

def show_window():
    stddraw.show(1 / FPS)

def add_points(points: int):
    global score
    score += points

def draw_score():
    
    x, y = 1, 9.7

    stddraw.setPenColor(stddraw.LIGHT_GRAY)
    stddraw.setFontSize(20)
    stddraw.text(x + 0.02, y - 0.02, f"Score: {score}")

    stddraw.setPenColor(stddraw.CYAN)
    stddraw.text(x, y, f"Score: {score}")

def main():
    pass

if __name__ == "__main__":
    main()
