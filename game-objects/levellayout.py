import gamewindow

VX = 0.025
VY = -0.1
PVX = -0.0125

# LVL 1

# READ IN FROM DATA FILE, STORE VALS

with open(LVL1_ENEMIES, mode='rb') as file: # b is important -> binary
    fileContent = file.read()

#TODO: struct.unpack('iiii', fileContent[:20]) ???

# LVL 2

with open(LVL2_ENEMIES, mode='rb') as file: # b is important -> binary
    fileContent = file.read()

# LVL 3

with open(LVL3_ENEMIES, mode='rb') as file: # b is important -> binary
    fileContent = file.read()

# LVL 4

with open(LVL4_ENEMIES, mode='rb') as file: # b is important -> binary
    fileContent = file.read()

# LVL 5 - BOSS

with open(LVL5_ENEMIES, mode='rb') as file: # b is important -> binary
    fileContent = file.read()

def main():
    pass

if __name__ == "__main__":
    main()
