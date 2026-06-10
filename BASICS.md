# Shortcuts for basic operations

```
union()(a, b) == a + b
difference()(a, b) == a - b
intersection()(a, b) == a & b
```

# DXF extrusions

In QCAD:
* Delete all spaces except for the "Model" space (the automatically created "Paper" space fi.)
* Explode polylines (it might work for a single object, but fail when trying to do a difference on it)
* Save as DXF version 13

```
linear_extrude(thickness)(import_(dxf_file))
```
