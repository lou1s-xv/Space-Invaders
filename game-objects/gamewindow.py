import stddraw
import struct

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
    stddraw.show(1000 / FPS)

def add_points(points: int):
    global score
    score += points

def draw_score():
    x, y = 1, 9.7

    stddraw.setPenColor(stddraw.DARK_BLUE)
    stddraw.setFontSize(20)
    stddraw.text(x + 0.02, y - 0.02, f"Score: {score}")

    stddraw.setPenColor(stddraw.CYAN)
    stddraw.text(x, y, f"Score: {score}")

def game_over():
    
    # updating binary file with new hs
    f = open('hs', 'rb')
    ln = f.read()
    hs = int(ln)
    f.close()
    if score > hs:
        hs = score
        f = open('hs', 'rb')
        bin = struct.pack("i", hs)
        f.write(bin)
        f.close()

    #code for screen goes here

def main():
    pass

if __name__ == "__main__":
    main()
