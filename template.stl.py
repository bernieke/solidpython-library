#!/usr/bin/env python3

from solid2 import *


obj = cube(1, 1, 1)


if __name__ == '__main__':
    with open(__file__[:-7] + '.scad', 'w') as f:
        f.write(scad_render(obj, file_header='$fa = 1;\n$fs = 0.4;\n'))
