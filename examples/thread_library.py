#!/usr/bin/env python3

from solid2 import cylinder, import_scad


threads = import_scad('threadlib/threadlib.scad')

cylinder(10, 10) - threads.tap('M18', 5)
threads.bolt('M18', 5)
