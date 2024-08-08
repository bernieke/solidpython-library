#!/usr/bin/env python3

"""Creates a rounded cube between X=0, Y=0, Z=0 and X=width, Y=depth, Z=height.
"""

from solid2 import cylinder


def rounded_cube(width, depth, height, corner_radius):
    return (
        cylinder(r=corner_radius, h=height)
        + (cylinder(r=corner_radius, h=height)
           .translate([width - (corner_radius * 2), 0]))
        + (cylinder(r=corner_radius, h=height)
           .translate([width - (corner_radius * 2),
                       depth - (corner_radius * 2)]))
        + (cylinder(r=corner_radius, h=height)
           .translate([0, depth - (corner_radius * 2)]))
    ).hull().translate([corner_radius, corner_radius])
