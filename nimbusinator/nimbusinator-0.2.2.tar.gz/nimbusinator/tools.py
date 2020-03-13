import inspect
from pygame import image
from PIL import Image
import numpy as np


# Let there be ASCII art
logo = """                                        
 _____ _       _           _         _           
|   | |_|_____| |_ _ _ ___|_|___ ___| |_ ___ ___ 
| | | | |     | . | | |_ -| |   | .'|  _| . |  _|
|_|___|_|_|_|_|___|___|___|_|_|_|__,|_| |___|_|  
                                                  
                                               
RM Nimbus GUI for Python
                                            
"""


def message(silent, text):
    """Debug message

    Prints a message in the console including the name of the function
    that sent the message.

    Args:
        silent (bool): Pass if in silent mode
        text (str): The text of the message

    """

    # Pass if in silent model
    if silent:
        return
        
    # Get name of function that sent the message
    caller = inspect.stack()[1][3]
    # Print the debug message
    print('[nimbusinator] {}: {}'.format(caller, text))


def pil_to_pygame_image(PIL_image):
    """Convert PIL image to pygame surface

    Args:
        PIL_image (PIL.Image): The PIL image to be converted

    Returns:
        (pygame.image): The pygame image
    
    """

    return image.fromstring(PIL_image.tobytes(), PIL_image.size, PIL_image.mode)


def fix_coord(screen_size, coord):
    """Fix coordinates for use in OpenCV's drawing functions

    PIL images have upside-down co-ordinates and it shafts me
    every goddamn time, so this function "deals with it"

    Args:
        screen_size (tuple): The screen size (width, height)
        coord (tuple): The x, y coordinate to fix (x, y)

    Returns:
        (tuple): The coordinates flipped upside-down

    """
    
    return (coord[0], ((screen_size[1] - 1) - coord[1]))


def is_valid_colour(nimbus, colour):
    """Validate colour number

    If the colour number is out of range for the current screen
    mode a fatal error is yielded

    Args:
        nimbus (Nimbus): The Nimbus object
        colour (int): The colour number
    
    Returns:
        (bool): The test result

    """

    # validate low-res colour
    if nimbus.screen_mode == 'lo':
        if colour >= 0 and colour <= 15:
            # it's fine
            return True
        else:
            # it's not
            return False
    
    # validate high-res colour
    if nimbus.screen_mode == 'hi':
        if colour >= 0 and colour <= 3:
            # it's fine
            return True
        else:
            # it's not
            return False


def colrows_to_xy(screen_size, cursor_position):
    """Convert cursor position to x, y pixel position

    Args:
        screen_size (tuple): The screen size (width, height)
        cursor_position (tuple): The cursor position (row, col)

    Returns:
        (tuple): The screen position in pixels (x, y)
    
    """

    x = (8 * (cursor_position[0] - 1))
    y = (screen_size[1] - 2) - (cursor_position[1] * 10)
    return (x, y)


def ceildiv(a, b):
    return -(-a // b)


def char_image_selecta(font_img, ascii_code, font):
    """Get the image of a character from a PNG

    Enter an ASCII code and a transparent PNG image of the char is returned.
    Codes < 33 and delete char (127) just return a space.

    Args:
        ascii_code (int): The ASCII code (extended) of the character
        font (int): The font or charset

    Returns:
        (PIL image): The transparent image of the character
    
    """

    # On our Nimbus char map PNGs delete (127) is just a blank space, so if we
    # receive any < 33 control chars, set the ascii value to 127 so a space is
    # also returned in those cases.
    if ascii_code < 33:
        ascii_code = 127
    # Calculate the row and column position of the char on the character map PNG
    map_number = ascii_code - 32    # codes < 33 are not on the map (unprintable)
    row = ceildiv(map_number, 30)
    column = map_number - (30 * (row - 1))
    # Calculate corners of box around the char
    x1 = (column - 1) * 10
    x2 = x1 + 10
    y1 = (row - 1) * 10
    y2 = y1 + 10
    # Chop out the char and return
    return font_img.crop((x1, y1, x2, y2))


def recolour(nimbus, img, colour1, colour2, has_alpha=False):
    """Replace one colour with another in an image"""

    # Unpack the image
    img = img.convert('RGBA')
    data = np.array(img)
    if has_alpha:
        r, g, b, a = data.T
    else:
        r, g, b = data.T

    # Unpack colour1 and 2
    r1, g1, b1 = colour1

    # Replace white with red... (leaves alpha values alone...)
    white_areas = (r == r1) & (b == b1) & (g == g1)
    data[..., :-1][white_areas.T] = colour2

    return Image.fromarray(data)


def points_to_nparray(points_list):
    """Convert points_list from a set_points command into a numpy array"""

    empty = [255, 255, 255, 0]
    fill = [0, 0, 0, 255]

    rows = []

    for points in points_list:
        row = []
        for char in points:
            if char == '.':
                row.append(fill)
            if char == ' ':
                row.append(empty)
        rows.append(row)

    return np.array(rows, dtype=np.uint8)