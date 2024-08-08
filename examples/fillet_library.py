#!/usr/bin/env python3

import os

from solid2 import cube, import_scad

HOME = os.environ['HOME']

ENABLE_FILLETS = 0  # Set to 0 for quicker turnaround during development
ROUNDING_RADIUS = 1
LAYER_HEIGHT = 0.1

fillet = import_scad(f'{HOME}/git/other/openscad-fillets/fillets3d.scad')

obj = cube(10, 10, 10)
obj = fillet.topFillet(
    t=10,
    r=ROUNDING_RADIUS,
    s=ROUNDING_RADIUS / LAYER_HEIGHT,
    e=ENABLE_FILLETS)
