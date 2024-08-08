#!/usr/bin/env python3

"""Creates a fillet hole in Z direction, with the corner on X=0, Y=0.

Oriented for the furthest corner in both X and Y.

So to place this fillet on the furthest corner you translate it to
that corner's X and Y position.

To place it on another corner you rotateZ it before translation.
"""

from solid2 import cube, cylinder

from .common import C


def fillet(radius, height):
    height += C * 2  # Make bigger to go completely through bottom and top
    return (
        cube(radius, radius, height)
        - cylinder(r=radius, h=height + C * 2).translateZ(-C)
    ).translate(C - radius, C - radius, -C)  # Offset to go through the bottom
