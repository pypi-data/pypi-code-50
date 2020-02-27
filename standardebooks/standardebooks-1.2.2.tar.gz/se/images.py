#!/usr/bin/env python3
"""
Defines various functions useful for image processing tasks common to epubs.
"""

from pathlib import Path
import tempfile

import regex
from cairosvg import svg2svg
from PIL import Image, ImageMath
from svgpathtools import parse_path

import se
import se.formatting


LETTER_SPACING = 6.25 # In px; must match the letter-spacing value in titlepage and cover page CSS
DPI_MODIFIER = 1.25

def _color_to_alpha(image: Image, color=None) -> Image:
	"""
	Implements GIMP's color to alpha algorithm.
	See https://stackoverflow.com/a/1617909
	GPLv3: http://bazaar.launchpad.net/~stani/phatch/trunk/annotate/head:/phatch/actions/color_to_alpha.py#L50

	INPUTS
	image: A PIL image to work on
	color: A 4-tuple (R, G, B, A) value as the color to change to alpha

	OUTPUTS
	A string of XML representing the new SVG
	"""

	image = image.convert("RGBA")

	color = list(map(float, color))
	img_bands = [band.convert("F") for band in image.split()]

	# Find the maximum difference rate between source and color. I had to use two
	# difference functions because ImageMath.eval only evaluates the expression
	# once.
	alpha = ImageMath.eval(
		"""float(
		    max(
		        max(
		            max(
		                difference1(red_band, cred_band),
		                difference1(green_band, cgreen_band)
		            ),
		            difference1(blue_band, cblue_band)
		        ),
		        max(
		            max(
		                difference2(red_band, cred_band),
		                difference2(green_band, cgreen_band)
		            ),
		            difference2(blue_band, cblue_band)
		        )
		    )
		)""",
		difference1=lambda source, color: (source - color) / (255.0 - color),
		difference2=lambda source, color: (color - source) / color,
		red_band=img_bands[0],
		green_band=img_bands[1],
		blue_band=img_bands[2],
		cred_band=color[0],
		cgreen_band=color[1],
		cblue_band=color[2]
	)

	# Calculate the new image colors after the removal of the selected color
	new_bands = [
		ImageMath.eval(
			"convert((image - color) / alpha + color, 'L')",
			image=img_bands[i],
			color=color[i],
			alpha=alpha
		)
		for i in range(3)
	]

	# Add the new alpha band
	new_bands.append(ImageMath.eval(
		"convert(alpha_band * alpha, 'L')",
		alpha=alpha,
		alpha_band=img_bands[3]
	))

	new_image = Image.merge("RGBA", new_bands)

	background = Image.new("RGB", new_image.size, (0, 0, 0, 0))
	background.paste(new_image.convert("RGB"), mask=new_image)

	# SE addition: Lastly, convert transparent pixels to rgba(0, 0, 0, 0) so that Pillow's
	# crop function can detect them.
	# See https://stackoverflow.com/a/14211878
	pixdata = new_image.load()

	width, height = new_image.size
	for image_y in range(height):
		for image_x in range(width):
			if pixdata[image_x, image_y] == (255, 255, 255, 0):
				pixdata[image_x, image_y] = (0, 0, 0, 0)

	return new_image

def svg_text_to_paths(svg_xml: str) -> str:
	"""
	Convert SVG <text> elements to <path>s with cairosvg

	INPUTS
	svg_xml: An SVG file as a string

	OUTPUTS
	A string of XML representing the new SVG
	"""

	# Save the title for later, as cairosvg removes it
	try:
		title_element = regex.findall(r"<title>.+?</title>", svg_xml)[0]
	except:
		raise se.InvalidInputException("titlepage.svg is missing the <title> element.")

	# Now transform text to paths
	# dpi=90 is a magic number. Not sure why we need to specify this.
	processed_svg_xml = svg2svg(bytestring=svg_xml.encode(), dpi=90).decode()

	# cairosvg has a bug where text that has letter-spacing is not centered correctly.
	# To work around that, we try to calculate the width of each line, then center it manually by
	# moving each character left individually.

	canvas_width = se.TITLEPAGE_WIDTH / DPI_MODIFIER

	# Now iterate over each line and center it
	for line in set(regex.findall(r"<g style=\"[^\"]+?\">\s+<use .*?y=\"([^\"]+?)\"", processed_svg_xml, flags=regex.DOTALL)):
		# Get the first and last glyph ID for later
		matches = regex.findall(fr"<use xlink:href=\"#([^\"]+?)\" x=\"([^\"]+?)\" y=\"{line}\"", processed_svg_xml)
		first_glyph_id = matches[0][0]
		last_glyph_id = matches[len(matches) - 1][0]

		# Calculate the line width in native units (pt), except for the last char
		base_x = float(matches[0][1])
		line_width = float(matches[len(matches) - 1][1]) - base_x

		# Get the width of the first char; for some reason its path might be in a negative axis, so we have to adjust for that
		matches = regex.findall(fr"<symbol .*?id=\"{first_glyph_id}\">\s*<path .*?d=\"([^\"]+?)\"", processed_svg_xml, flags=regex.DOTALL)
		path = parse_path(matches[0])
		bbox = path.bbox()
		line_width += bbox[0] + (LETTER_SPACING * DPI_MODIFIER) # cairosvg outputs in pt, so we have to adjust with a DPI modifier

		# Get the width of the last char and then the final line width
		matches = regex.findall(fr"<symbol .*?id=\"{last_glyph_id}\">\s*<path .*?d=\"([^\"]+?)\"", processed_svg_xml, flags=regex.DOTALL)
		path = parse_path(matches[0])
		bbox = path.bbox()
		line_width += bbox[1] - bbox[0]

		# This is how much we have to pull the line left
		x_modifier = (base_x - ((canvas_width - line_width) / 2))

		# Now iterate over the chars in the line and move them all left by the modifier amount
		matches = regex.findall(fr"<use xlink:href=\"#([^\"]+?)\" x=\"([^\"]+?)\" y=\"{line}\"", processed_svg_xml)

		for match in matches:
			last_glyph_id = match[0]
			char_x = float(match[1])
			new_x = char_x - x_modifier
			processed_svg_xml = regex.sub(fr"<use xlink:href=\"#{last_glyph_id}\" x=\"{char_x}\" y=\"{line}\"", f"<use xlink:href=\"#{last_glyph_id}\" x=\"{new_x}\" y=\"{line}\"", processed_svg_xml)

	# Done re-centering text. Now clean up some of cairosvg's output cruft
	processed_svg_xml = regex.sub(r"</?g[^>]*?>", "", processed_svg_xml)
	processed_svg_xml = regex.sub(r" style=\"[^\"]*?\"", "", processed_svg_xml)
	processed_svg_xml = regex.sub(r" overflow=\"visible\"", "", processed_svg_xml)
	processed_svg_xml = regex.sub(r"<symbol id=\"glyph[\d]+-[\d]+\">\s*<path d=\"\"/>\s*</symbol>", "", processed_svg_xml, flags=regex.DOTALL)
	processed_svg_xml = processed_svg_xml.replace(" \"/>", "\"/>")

	# Re-add the title element
	processed_svg_xml = regex.sub(r"(<svg.+?>)", fr"\1{title_element}", processed_svg_xml)

	# Last cleanup
	processed_svg_xml = se.formatting.format_xhtml(processed_svg_xml)

	return processed_svg_xml

# Note: We can't type hint driver, because we conditionally import selenium for performance reasons
def render_mathml_to_png(driver, mathml: str, output_filename: Path) -> None:
	"""
	Render a string of MathML into a transparent PNG file.

	INPUTS
	driver: A Selenium webdriver, usually initialized from se.browser.initialize_selenium_firefox_webdriver
	mathml: A string of MathML
	output_filename: A filename to store PNG output to

	OUTPUTS
	None.
	"""

	with tempfile.NamedTemporaryFile(mode="w+") as mathml_file:
		with tempfile.NamedTemporaryFile(mode="w+", suffix=".png") as png_file:
			mathml_file.write(f"<!doctype html><html><head><meta charset=\"utf-8\"><title>MathML fragment</title></head><body>{mathml}</body></html>")
			mathml_file.seek(0)

			driver.get(f"file://{mathml_file.name}")
			# We have to take a screenshot of the html element, because otherwise we screenshot the viewport, which would result in a truncated image
			driver.find_element_by_tag_name("html").screenshot(png_file.name)

			image = Image.open(png_file.name)
			image = _color_to_alpha(image, (255, 255, 255, 255))
			image.crop(image.getbbox()).save(output_filename)

def remove_image_metadata(filename: Path) -> None:
	"""
	Remove exif metadata from an image.

	INPUTS
	filename: A filename of an image

	OUTPUTS
	None.
	"""

	image = Image.open(filename)
	data = list(image.getdata())

	image_without_exif = Image.new(image.mode, image.size)
	image_without_exif.putdata(data)
	image_without_exif.save(filename, subsampling="4:4:4")
