import math
#Data for reference:

#miscellaneous
DT = 20.0
RADIUS = 0.45 #wall check condition

#title screen constants
t_vx = 0.05 #speed on title screen
tw = 0.25 #starting width on title screen
th = 0.25 #starting height on title screen

#Enemy constants
ENEMY_SIZE = 0.5
gen_vx = 1
gen_vy = -5
mvx = -0.75

SHOOTER_SIZE = 0.5
SHOOTER_SPEED = 15
SHOOTER_DIST = 0.1
ANGLE_STEP = math.pi / 90


#Level 1 constants for enemies
l1_rows = 2
l1_cols = 8
l1_spacing = 0.55
l1_vx = 0.75
l1_vy = -3
l1_xstart = 2
l1_ystart = 8

#Level 2 constants for enemies
l2_rows = 5
l2_cols = 10 
l2_spacing = 0.55
l2_vx = 0.75
l2_vy = -3
l2_xstart = 3
l2_ystart = 8


#Level 3 constants for enemies
l3_pattern = [1, 3, 5, 3, 1]
l3_xcen = 5
l3_ystart = 8
l3_spacing = 0.55
l3_vx = 0.75
l3_y = -3

#Level 4 constants for enemies
l4_rows = 8
l4_cols = 8
l4_xstart = 3
l4_ystart = 8
l4_spacing = 0.55
l4_vx = 0.75
l4_vy = -3

