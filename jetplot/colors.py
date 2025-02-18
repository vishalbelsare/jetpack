"""Colorschemes"""

from collections import namedtuple
from matplotlib import cm
import numpy as np


__all__ = ["cmap_colors"]


Color = namedtuple("Color", ("v1", "v2", "v3", "v4", "v5", "v6", "v7", "v8", "v9"))
black = "#000000"
white = "#ffffff"

gray = Color(
    "#f7fafc",
    "#edf2f7",
    "#e2e8f0",
    "#cbd5e0",
    "#a0aec0",
    "#718096",
    "#4a5568",
    "#2d3748",
    "#1a202c",
)
red = Color(
    "#fff5f5",
    "#fed7d7",
    "#feb2b2",
    "#fc8181",
    "#f56565",
    "#e53e3e",
    "#c53030",
    "#9b2c2c",
    "#742a2a",
)
orange = Color(
    "#fffaf0",
    "#feebc8",
    "#fbd38d",
    "#f6ad55",
    "#ed8936",
    "#dd6b20",
    "#c05621",
    "#9c4221",
    "#7b341e",
)
yellow = Color(
    "#fffff0",
    "#fefcbf",
    "#faf089",
    "#f6e05e",
    "#ecc94b",
    "#d69e2e",
    "#b7791f",
    "#975a16",
    "#744210",
)
green = Color(
    "#f0fff4",
    "#c6f6d5",
    "#9ae6b4",
    "#68d391",
    "#48bb78",
    "#38a169",
    "#2f855a",
    "#276749",
    "#22543d",
)
teal = Color(
    "#e6fffa",
    "#b2f5ea",
    "#81e6d9",
    "#4fd1c5",
    "#38b2ac",
    "#319795",
    "#2c7a7b",
    "#285e61",
    "#234e52",
)
blue = Color(
    "#ebf8ff",
    "#bee3f8",
    "#90cdf4",
    "#63b3ed",
    "#4299e1",
    "#3182ce",
    "#2b6cb0",
    "#2c5282",
    "#2a4365",
)
indigo = Color(
    "#ebf4ff",
    "#c3dafe",
    "#a3bffa",
    "#7f9cf5",
    "#667eea",
    "#5a67d8",
    "#4c51bf",
    "#434190",
    "#3c366b",
)
purple = Color(
    "#faf5ff",
    "#e9d8fd",
    "#d6bcfa",
    "#b794f4",
    "#9f7aea",
    "#805ad5",
    "#6b46c1",
    "#553c9a",
    "#44337a",
)
pink = Color(
    "#fff5f7",
    "#fed7e2",
    "#fbb6ce",
    "#f687b3",
    "#ed64a6",
    "#d53f8c",
    "#b83280",
    "#97266d",
    "#702459",
)

rainbow = (blue, orange, green, red, purple, teal, pink, indigo, yellow)
bright = (r.v4 for r in rainbow)
dark = (r.v6 for r in rainbow)


def cmap_colors(cmap: str, n: int, vmin: float=0., vmax: float=1.):
    return cm.__getattribute__(cmap)(np.linspace(vmin, vmax, n))
