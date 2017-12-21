#!/usr/bin/env python3

import math
"""VRMLで使う円の座標を求める


"""
CENTER_X = 12
CENTER_Y = 2.5
R = 5.5
i = 36
for angle in range(i):
    x = CENTER_X + (math.cos(angle*2/i*math.pi))
    y = CENTER_Y + (math.sin(angle*2/i*math.pi))
    print(str(x) + "\t" + str(y) + "\t0,")


