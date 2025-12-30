#!/usr/bin/env python3

from solid2 import *

from solidpython_library import C


obj = (
    cube(1, 1, 1)
    - cylinder(d=0.5, h=1 + 2 * C).translate(0.5, 0.5, -C)
)


if __name__ == '__main__':
    with open(__file__[:-7] + '.scad', 'w') as f:
        f.write(scad_render(obj, file_header='$fa = 1;\n$fs = 0.4;\n'))
