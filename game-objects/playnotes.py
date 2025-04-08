import sys
import math
import stdio, stdarray, stdrandom, stddraw, stdaudio  # type: ignore

def tone(freq: float, t: float) -> list[float]:

    s: list[float] = [0] * int(44100 * t)
    for i in range(len(s)):
        s[i] = math.sin(freq *(2 * math.pi * i)/44100 )
    return s

def explosion(t: float) -> list[float]:

    n = int(44100 * t)
    samples = stdarray.create1D(n, 0.0)

    for i in range(n):
        decay = 1.0 - i/n
        samples[i] = decay * stdrandom.uniformFloat(-1.0, 1.0)

    return samples

def main() -> None:  # Need the return type for mypy to type-check the body

    freq: float = float(sys.argv[1])
    duration: float = float(sys.argv[2])
    displacements: list[float] = tone(freq, duration)
    stdaudio.playSamples(displacements)

if __name__ == "__main__":
    main()
