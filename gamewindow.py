import stddraw
import stdaudio
import struct
import math
import time
from picture import Picture
import threading

X_MIN = 0
X_MAX = 10
Y_MIN = 0
Y_MAX = 10
FPS = 30
score = 0
GAME_END = False
music_thread = None
HEART_WIDTH = 0.75
HEART_DIST = 0.25

def init():
    stddraw.setXscale(X_MIN, X_MAX)
    stddraw.setYscale(Y_MIN, Y_MAX)

def show_window():
    stddraw.show(1000 / FPS)

def clear_window():
    stddraw.clear(stddraw.BLACK)

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

def draw_health(health):
    heart = Picture("heart_icon.png")
    for i in range(health):
        stddraw.picture(heart, X_MAX - i * (HEART_WIDTH + HEART_DIST), Y_MAX - (HEART_WIDTH + HEART_DIST), HEART_WIDTH, HEART_WIDTH)
        

def game_over():
    
    # updating binary file with new hs
    f = open('hs', 'rb')
    hs = struct.unpack('i', f.read(4))[0]
    f.close()
    if score > hs:
        hs = score
        f = open('hs', 'rb')
        bin = struct.pack("i", hs)
        f.write(bin)
        f.close()

    #code for screen goes here
    stddraw.clear(stddraw.BLACK)
    stddraw.setPenColor(stddraw.WHITE)

    stddraw.picture(Picture("Fatality.png"), 5, 6, 7, 7)
    threading.Thread(target=stdaudio.playFile, args=("GameOverSound",)).start()
    stddraw.setFontSize(40)
    stddraw.text(5, 2, "High Score: " + str(hs))

    stddraw.show(10000)

def player_win():
    
    threading.Thread(target=stdaudio.playFile, args=("PlayerWinSound",)).start()
    stddraw.clear(stddraw.BLACK)
    stddraw.setPenColor(stddraw.WHITE)
    stddraw.filledRectangle(2, 2, 6, 6)
    stddraw.setPenColor(stddraw.CYAN)
    stddraw.rectangle(2, 2, 6, 6)
    stddraw.picture(Picture("Soldier.png"), 5, 5, 6, 6)
    stddraw.picture(Picture("Victory.png"), 5, 5, 4, 4)
    stddraw.picture(Picture("Fortnite.png"), 2, 8, 4, 2)

    stddraw.show(10000)


def play_game_music():
    while not GAME_END:
        stdaudio.playFile("Street Fighter II Arcade Music")
def start_game_music():
    global music_thread
    music_thread = threading.Thread(target=play_game_music)
    music_thread.start()

def show_loading_screen(level_num):
    """Displays an animated loading screen with level-specific message"""
    stddraw.clear(stddraw.BLACK)
    
    # Loading screen elements
    base_text = f"LOADING LEVEL {level_num}"
    animated_text = base_text
    progress = 0.0
    start_time = time.time()
    loading_complete = False
    
    # Animation parameters
    total_duration = 10  # seconds
    pulse_frequency = 2.0  # dots animation speed
    
    # Loading animation loop
    while not loading_complete:
        elapsed = time.time() - start_time
        progress = min(elapsed / total_duration, 1.0)
        loading_complete = (progress >= 1.0)
        
        # Clear and redraw each frame
        stddraw.clear(stddraw.BLACK)
        
        # Draw game title
        stddraw.setPenColor(stddraw.CYAN)
        stddraw.setFontSize(30)
        stddraw.text(5, 7, "SPACE INVADERS")
        
        # Draw animated loading text
        stddraw.setPenColor(stddraw.WHITE)
        stddraw.setFontSize(20)
        
        # Pulsing dots animation
        dot_count = int((time.time() * pulse_frequency) % 4)
        animated_text = base_text + "." * dot_count
        stddraw.text(5, 5, animated_text)
        
        # Progress bar
        bar_width = 6.0
        bar_height = 0.4
        stddraw.setPenColor(stddraw.DARK_GRAY)
        stddraw.filledRectangle(2, 3, bar_width, bar_height)  # Background
        
        stddraw.setPenColor(stddraw.GREEN)
        stddraw.filledRectangle(2, 3, bar_width * progress, bar_height)  # Progress
        
        # Percentage counter
        stddraw.setPenColor(stddraw.YELLOW)
        stddraw.text(5, 2, f"{int(progress * 100)}%")
        
        # Level-specific tip (optional)
        stddraw.setPenColor(stddraw.LIGHT_GRAY)
        stddraw.setFontSize(14)
        stddraw.text(5, 1, _get_level_tip(level_num))
        
        stddraw.show(50)  # 50ms frame delay (~20 FPS)
    
    # Completion flash
    stddraw.clear(stddraw.BLACK)
    stddraw.setPenColor(stddraw.GREEN)
    stddraw.setFontSize(24)
    stddraw.text(5, 5, f"LEVEL {level_num} READY!")
    stddraw.show(500)  # Show for 0.5 seconds

def _get_level_tip(level_num):
    """Returns level-specific loading tips"""
    tips = {
        1: "Tip: Aim carefully at the formation patterns!",
        2: "Tip: Enemies are on the lose, WATCH OUT!",
        3: "Tip: Use bunkers for temporary protection!",
        4: "Tip: The boss is las YOU can take him!"
    }
    return tips.get(level_num, "Tip: Destroy all enemies to advance!")



    stddraw.clear(stddraw.DARK_GRAY)

    stddraw.picture(Picture("Splat.png"), 5, 5, 4, 4)
    stddraw.picture(Picture("Fatality.png"), 5, 5, 4, 4)
    threading.Thread(target=stdaudio.playFile, args=("something",))
    stddraw.picture(Picture("dead_soldier.png"), 2, 9, 1, 1)

    stddraw.show(10000)


def main():
    pass
if __name__ == "__main__":
    main()
