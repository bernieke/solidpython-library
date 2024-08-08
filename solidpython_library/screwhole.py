#!/usr/bin/env python3

"""Creates a screwhole in Z direction, centered on X=0, Y=0.

If the screw is countersunk, the head will be on top.
"""

from solid2 import cylinder

from .common import C


class SCREW_CONFIG:

    class M3_INTO:
        countersunk = False
        diameter = 2.7

    class M3_THROUGH:
        countersunk = False
        diameter = 3

    class SPAX_T15:
        countersunk = True
        diameter = 4
        head_diameter = 6.8
        head_depth = 3.2


def screwhole(length, screw):
    length += C * 2  # Make bigger to go completely through bottom and top
    obj = cylinder(r=screw.diameter / 2, h=length)  # Screw hole
    if screw.countersunk:
        obj += (cylinder(r1=screw.diameter / 2,
                         r2=screw.head_diameter / 2,
                         h=screw.head_depth)
                .translateZ(length - screw.head_depth))  # Head hole
    return obj.translateZ(-C)  # Offset to go through at the bottom
