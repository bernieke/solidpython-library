#!/usr/bin/env python3

"""Creates a hole for a heatset insert in Z direction, centered on X=0, Y=0.

If length is larger than the heatset insert, the screwhole will be extended.

The insert will be on top.

If there are mating surfaces, the holes must be smaller than the insert hole.
So that the insert carries the load, and not the plastic around it!
In case of the M3 heatset insert this means the hole must be between 3 and 4mm.
(Use 3mm for a tight fit, 3.5mm for a loose fit.)
"""

from solid2 import cylinder

from .common import C


class HEATSET_INSERT_CONFIG:

    class M3:
        headed = False  # Whether the insert has a head (or collar)
        screw = 3       # Screw diameter, to continue the hole after the insert
        hole = 4.25     # Hole diameter to fit the insert (see specifications)
        length = 5      # Insert length (including the head)
        head_diameter = 0     # Counterbore diameter
        head_height = 0       # Counterbore height


def heatset_insert(length, insert=HEATSET_INSERT_CONFIG.M3):
    # The hole for the insert needs to be 1mm deeper than the insert length
    # The length must be at least the depth of the insert hole
    length = max(length, insert.length + 1)
    length += C * 2  # Make bigger to go completely through bottom and top
    obj = (
        cylinder(r=insert.screw / 2, h=length)  # Screw hole
        + (cylinder(r=insert.hole / 2, h=insert.length + 1)
           .translateZ(length - (insert.length + 1)))  # Insert hole
    )
    if insert.headed:
        obj += (cylinder(r=insert.head_diameter / 2, h=insert.head_height)
                .translateZ(length - insert.head_height))  # Head counterbore
    return obj.translateZ(-C)  # Offset to go through at the bottom
