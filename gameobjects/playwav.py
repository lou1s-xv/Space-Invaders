import sys
import math
import stdio, stdarray, stdrandom, stddraw, stdaudio  # type: ignore

def play(file: str):
    stdaudio.playFile(file)


def main() -> None:  # Need the return type for mypy to type-check the body

    name = sys.argv[1]
    play(name)

if __name__ == "__main__":
    main()
