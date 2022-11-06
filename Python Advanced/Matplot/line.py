import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, linestyle='dotted', c='hotpink')
plt.show()

# #
# Shorter Syntax
# The line style can be written in a shorter syntax:
#
# linestyle can be written as ls.
#
# dotted can be written as :.
#
# dashed can be written as --.
#
# Line Styles
# You can choose any of these styles:
#
# Style	Or
# 'solid' (default)	'-'
# 'dotted'	':'
# 'dashed'	'--'
# 'dashdot'	'-.'
# 'None'	'' or ' '
