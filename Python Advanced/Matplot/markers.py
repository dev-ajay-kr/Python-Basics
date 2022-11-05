import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o')
plt.show()


ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, '*:g')   # (points, 'style:color'
plt.show()

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r')   #ms is marker size mec markeredge color
plt.show()

##
#
# Line Reference
# Line Syntax	Description
# '-'	Solid line
# ':'	Dotted line
# '--'	Dashed line
# '-.'	Dashed/dotted line


#########
# #Marker Reference
# You can choose any of these markers:
#
# Marker	Description
# 'o'	Circle
# '*'	Star
# '.'	Point
# ','	Pixel
# 'x'	X
# 'X'	X (filled)
# '+'	Plus
# 'P'	Plus (filled)
# 's'	Square
# 'D'	Diamond
# 'd'	Diamond (thin)
# 'p'	Pentagon
# 'H'	Hexagon
# 'h'	Hexagon
# 'v'	Triangle Down
# '^'	Triangle Up
# '<'	Triangle Left
# '>'	Triangle Right
# '1'	Tri Down
# '2'	Tri Up
# '3'	Tri Left
# '4'	Tri Right
# '|'	Vline
# '_'	Hline


# Color Reference
# Color Syntax	Description
# 'r'	Red
# 'g'	Green
# 'b'	Blue
# 'c'	Cyan
# 'm'	Magenta
# 'y'	Yellow
# 'k'	Black
# 'w'	White


