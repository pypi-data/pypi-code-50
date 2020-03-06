from .hsvcolor import HSVColor
from .rgbcolor import RGBColor


def rgb_to_hsv(rgb):
    """Converts a color from RGB to HSV colorspace.

	:param rgb: The color to be converted. Accepted types are list, tuple and RGBColor. If a list or a tuple is provided, 
		the values must be int values or at least covertable to int. The values have to be within the range [0,255]

	:type rgb: (Color, list, tuple)
	"""
    if isinstance(rgb, RGBColor):
        return HSVColor(*rgb.hsv)
    if isinstance(rgb(list, tuple)) and len(rgb) == 3:
        return HSVColor(RGBColor(*rgb).hsv)


def hsv_to_rgb(hsv):
    """Converts a color from HSV to RGB colorspace.

	:param rgb: The color to be converted. Accepted types are list, tuple and Color. If a list or a tuple is provided, 
		the values must be int values or at least covertable to int. The hue value has to be within the range [0,360[.
		The values for saturation and value have to be within the range [0,100]

	:type rgb: (Color, list, tuple)
	"""
    if isinstance(hsv, HSVColor):
        return RGBColor(*hsv.rgb)
    if isinstance(hsv(list, tuple)) and len(hsv) == 3:
        return RGBColor(*(HSVColor(*hsv).rgb))
