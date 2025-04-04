import sys
import math
import stdio, stdarray, stdrandom, stddraw, stdaudio  # type: ignore
import playnotes

def superpose(a: list[float], b: list[float], a_wt: float, b_wt: float) -> list[float]:
    
    #creates meshed harmonic template list
    c = [0] * len(a)
    
    #fills that list with the meshed harmonic
    for i in range(len(c)):
        c[i] = a_wt*a[i] + b_wt*b[i]
    
    return c

def chord(freq: float, time: float) -> list[float]:
    
    pure_note: list[float] = playnotes.tone(freq, time)
    octave_up: list[float] = playnotes.tone(2*freq, time)
    octave_down: list[float] = playnotes.tone(0.5*freq, time)
    harmonic: list[float] = superpose(octave_up, octave_down, 0.5, 0.5)
    final: list[float] = superpose(harmonic, pure_note, 0.5, 0.5)

    return final


def main() -> None:  # Need the return type for mypy to type-check the body

    while not stdio.isEmpty():
        note = stdio.readInt()
        freq = 440 * 2**(note/12)
        time = stdio.readFloat()
        final = chord(freq, time)
        stdaudio.playSamples(final)


if __name__ == "__main__":
    main()
