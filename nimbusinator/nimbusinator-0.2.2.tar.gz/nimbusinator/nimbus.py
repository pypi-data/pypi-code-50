import os
import sys
import time
import contextlib
with contextlib.redirect_stdout(None):
    import pygame
import copy
import numpy as np
from .tools import logo, message, pil_to_pygame_image, fix_coord, char_image_selecta, colrows_to_xy, recolour, points_to_nparray
from .colour_table import colour_table, default_colours
from PIL import Image, ImageDraw, ImageColor
import threading
import random
from pynput import keyboard
import simpleaudio as sa
from .welcome import welcome
from .command import Command
from .supported_control_keys import supported_control_keys


# get full path of this script
real_path = os.path.dirname(os.path.realpath(__file__))


class Nimbus:
    """Nimbus video display class.

    This class represents the Nimbus video display that will host the user
    interface for your application.  When created, the new Nimbus object 
    will not be visible until the boot() method has been called.

    Args:
        full_screen (bool, optional): Full screen mode
        title (str, optional): The title of the display window
        border_size (int, optional): The thickness of the border in pixels (default is 40)
        silent (bool, optional): Run Nimbusinator in silent mode (default is False)

    """

    def __init__(self, full_screen=False, title='Nimbusinator', border_size=40, silent=False):
        """Create a new Nimbus object

        Args:
            full_screen (:obj:`bool`, optional): Full screen mode
            title (str, optional): The title of the display window
            border_size (int, optional): The thickness of the border in pixels (default is 40)
            silent (bool, optional): Run Nimbusinator in silent mode (default is False)
        """

        if not silent:
            print(logo)

        # Constants
        self.SCREEN_MODES = {                           # The absolute screen resolution for
            'hi': (640, 250),                           # high (80 column) and low-res (40
            'lo': (320, 250)                            # column) modes
            }
        self.FONT_IMAGES = self.__load_fonts()          # Font images
        self.RESOLVABLE_UNICODE_CHARS = {               # These unicode chars have an equivalent
            'ç': 128, 'ü': 129, 'é': 130,               # char in Nimbus' Extended ASCII. 
            'â': 131, 'ä': 132, 'à': 133,               
            'å': 134, 'ç': 135, 'ê': 136,
            'ë': 137, 'è': 138, 'ï': 139,
            'î': 140, 'ì': 141, 'Ä': 142,
            'Å': 143, 'É': 144, 'æ': 145,
            'Æ': 146, 'ô': 147, 'ö': 148, 
            'ò': 149, 'û': 150, 'ù': 151, 
            'ÿ': 152, 'Ö': 153, 'Ü': 154, 
            '¢': 155, '£': 156, '¥': 157, #    158,
            'ƒ': 159, 'á': 160, 'í': 161,
            'ó': 162, 'ú': 163, 'ñ': 164,
            'Ñ': 165, #    166,      167,
            '¿': 168, '½': 169, '¼': 170,
            '¦': 171, '«': 173, '»': 174,
            'α': 223, 'β': 224, 'Γ': 225,
            'π': 226, 'Σ': 227, 'σ': 228,
            'μ': 229, 'ϒ': 230, #    231,
            'ϴ': 232, 'Ω': 233, 'δ': 234,
            '∞': 235, #    236,
            '∈': 237, '∩': 238, '≡': 239,
            '±': 240, '≥': 241, '≤': 242,
            '⌠': 243, '⌡': 244, '÷': 245,
            '≈': 246, '°': 247, '·': 248, # 249,
            '√': 250, 'ⁿ': 251, '²': 252,
        }
        self.SUPPORTED_CONTROL_KEYS = supported_control_keys
        self.COLOUR_TABLE = colour_table                # This is the RGB colour table from the Nimbus
        self.DEFAULT_COLOURS = default_colours          # The default colours which cannot be changed during runtime
        self.NORMALIZED_PAPER_SIZE = (640, 500)         # After drawing graphics and chars the paper is normalized to this size
        # Background size is the normalized paper size plus 2x border size:
        background_width = self.NORMALIZED_PAPER_SIZE[0] + (2 * border_size)
        background_height = self.NORMALIZED_PAPER_SIZE[1] + (2 * border_size)
        self.BACKGROUND_SIZE = (background_width, background_height)
        # RM Nimbus logo
        logo_path = os.path.join(real_path, 'data', 'rm-nimbus-logo.bmp')
        self.NIMBUS_LOGO = Image.open(logo_path)
        self.CURSOR_IMAGE = Image.new(
            'RGB',
            (10, 2), 
            (0, 0, 0)
        )
        self.EMPTY_CHAR_IMAGE = Image.new(
            'RGB',
            (10, 10),
            (0, 0, 0)
        )

        # Settings
        self.full_screen = full_screen
        self.title = title
        self.border_size = border_size
        self.silent = silent

        # Variables
        self.screen_mode = 'hi'
        self.runtime_colours = copy.deepcopy(self.DEFAULT_COLOURS)   # These colours can be changed at runtime
        self.paper_colour = 1
        self.border_colour = 1
        self.brush_colour = 3
        self.pen_colour = 3
        self.charset = 0
        self.plot_font = 0
        self.cursor_position = (1, 1)
        self.cursor_enabled = False
        self.keyboard_buffer = []
        # Set up default and user-define points
        self.points_styles = self.__init_points_styles()
        self.points_style = 0
        self.control_char = ''
        self.image_blocks = [None] * 255

        # Initialize with empty paper
        self.paper_image = self.empty_paper()

        # Status flags
        self.running = False                          # Set to True to run the Nimbus and the display
        self.__cursor_flash = False                     # Make cursor visible if True
        self.ctrl_pressed = False
        self.enter_was_pressed = False
        self.backspace_was_pressed = False
        self.floppy_is_running = False


    def __init_points_styles(self):
        """Initialize a list of default points styles and empty styles"""

        styles = []
        for i in range(0, 256):
            styles.append(
                Image.new(
                    'RGBA',
                    (8, 8),
                    (255, 255, 255, 0)
                )       
            )
        return styles


    def __load_fonts(self):
        """Load fonts from PNG files

        Returns:
            (dict): A dict of PIL images for font 0 and font 1

        """

        fonts = {}
        for font in range(0, 2):
            font_img_path = os.path.join(real_path, 'data', 'font{}-alpha.png'.format(font))
            font_img = Image.open(font_img_path)
            fonts[font] = []
            for ascii_code in range(0, 256):
                fonts[font].append(char_image_selecta(font_img, ascii_code, font))
        return fonts


    def empty_paper(self):
        """Return empty paper filled with the current paper colour"""

        return Image.new(
            'RGB',
            self.SCREEN_MODES[self.screen_mode], 
            self.__get_rgb(self.paper_colour)
        )


    def __get_rgb(self, colour):
        """Get an RGB tuple for a given colour code and current screen mode

        Args:
            colours (int): The Nimbus colour
        
        Returns:
            (tuple): The RGB tuple

        """

        return self.COLOUR_TABLE[self.runtime_colours[self.screen_mode][colour]]


    def plonk_image_on_paper(self, img, coord, transparent=False):
        """Plonk a PIL image somewhere on the paper
        
        The passed coordinates are consistent with RM Nimbus implemented, i.e.
        bottom-left of screen = (0, 0) and any images are located relative to
        their bottom-left corner

        Args:
            img (PIL image): The image to be plonked
            coord (tuple): The coordinate tuple (x, y)
            transparent (bool, optional): True if image contains an alpha layer for transparency

        """

        # Flip y
        x, y = fix_coord(self.SCREEN_MODES[self.screen_mode], coord)

        # And change point-of-reference to bottom-left corner position
        y -= img.size[1]
        
        # Then paste image
        if transparent:
            self.paper_image.paste(img, (x, y), mask=img)
        else:
            self.paper_image.paste(img, (x, y))


    def __cycle_cursor_flash(self):
        """Cycle the cursor flash

        This needs to run in it's own thread

        """
        while self.running:
            # If the Nimbus is running flip cursor flash every 0.5 secs
            time.sleep(0.5)
            cursor_flash = self.__cursor_flash
            self.__cursor_flash = not cursor_flash
        return


    def __display_loop(self):
        """The display loop

        Normalize paper image.  Overlay normalized image on background
        image to make the video image.  If not in full screen mode
        just show the video image.  If in full screen mode scale the
        video image to the display height, overlay it on a background
        image that has the same dimensions as the display, and show.
        The loop breaks if self.running becomes false.  This method
        must be run in its own thread.

        """

        while self.running:
            # Overlay flash cursor if enabled
            paper_image_plus_cursor = self.paper_image.copy()
            if self.__cursor_flash and self.cursor_enabled:
                # Recolour cursor image to pen colour
                cursor_image = recolour(self, self.CURSOR_IMAGE, (0, 0, 0), self.COLOUR_TABLE[self.runtime_colours[self.screen_mode][self.pen_colour]], has_alpha=True)
                # Paste cursor image on paper_image_plus_cursor at x, y
                # Flip y
                x, y = fix_coord(self.SCREEN_MODES[self.screen_mode], colrows_to_xy(self.SCREEN_MODES[self.screen_mode], self.cursor_position))
                # Change point-of-reference to bottom-left corner position
                y -= 2
                # And paste cursor
                paper_image_plus_cursor.paste(cursor_image, (x, y))
            # Normalized paper image
            normalized_paper_image = paper_image_plus_cursor.resize(self.NORMALIZED_PAPER_SIZE, resample=Image.NEAREST)
            # Create background image with border colour
            background_image = Image.new(
                'RGB',
                self.BACKGROUND_SIZE,
                self.__get_rgb(self.border_colour)
            )
            # Overlay normalized paper image on background
            background_image.paste(normalized_paper_image, (self.border_size, self.border_size))
            # Handle full screen
            if self.full_screen:
                # Calculate new dimensions, resize and calculate x offset
                scale = self.__full_screen_display_size[1] / self.BACKGROUND_SIZE[1]
                new_size = (int(self.BACKGROUND_SIZE[0] * scale), self.__full_screen_display_size[1])
                background_image = background_image.resize(new_size, resample=Image.BICUBIC)
                display_x_offset = int((self.__full_screen_display_size[0] - new_size[0]) / 2)
            else:
                # Windows, so no x offset or resizing
                display_x_offset = 0
            # Create the video image, blit it and flip it
            video_image = pil_to_pygame_image(background_image)
            self.__pygame_display.blit(video_image, (display_x_offset, 0))
            pygame.display.flip()


    def __on_key_press(self, key):
        """Handle control key presses

        """
        
        # Printable chars go straight into the buffer
        try:
            self.keyboard_buffer.append(key.char)
            # BUT - if CTRL-C situation then shutdown!
            if self.ctrl_pressed and key.char.lower() == 'c':
                message(self.silent, 'CTRL-C detected')
                self.shutdown()
        except AttributeError:
            # Handle CTRL released
            if key == keyboard.Key.ctrl_l or keyboard.Key.ctrl_r:
                self.ctrl_pressed = True
            # Handle ENTER hit
            if key == keyboard.Key.enter:
                self.enter_was_pressed = True
            # Handle BACKSPACE hit
            if key == keyboard.Key.backspace:
                self.backspace_was_pressed = True
            # Also add spaces to buffer
            if key == keyboard.Key.space:
                self.keyboard_buffer.append(' ')
            # The following keys can be detected by gets by sending -1 to the 
            # buffer and logging the key in control_char
            for control_key, control_key_string in self.SUPPORTED_CONTROL_KEYS.items():
                if key == control_key:
                    self.keyboard_buffer.append(-1)
                    self.control_char = control_key_string
                    break



    def __on_key_release(self, key):
        """Handle control key releases

        """

        # Handle CTRL released
        if key == keyboard.Key.ctrl_l or keyboard.Key.ctrl_r:
            self.ctrl_pressed = False


    def __floppy_drive_effects(self):
        """Simulate floppy drive grinding

        This has to be run a thread.  Two drive sounds are supplied: a
        short 'dot' sounds, and a long 'dash' sound, with 4 variations
        of each.  Semi-random patterns of dashes and dots are generated 
        with randomly-selected variations while the floppy_is_running
        flag is True.

        """
        while self.running:
            # Load sound effects
            dash = []
            dot = []
            for i in range(1, 5):
                # Abort if shutting down
                if not self.running:
                    return
                # Otherwise load sound effects
                dash_path = os.path.join(real_path, 'data', 'floppy-dash{}.wav'.format(i))
                dot_path = os.path.join(real_path, 'data', 'floppy-dot{}.wav'.format(i))
                dash.append(sa.WaveObject.from_wave_file(dash_path))
                dot.append(sa.WaveObject.from_wave_file(dot_path))
            # If flag is True play a bunch of grinding floppy drive sounds
            if self.floppy_is_running and self.running:
                # play dash (pick one at random)
                play_obj = dash[random.randint(0, 3)].play()
                play_obj.wait_done()
                # Abort is shutting down
                if not self.running:
                    return
                # Otherwise play random number of dots
                for i in range(0, random.randint(1, 5)):
                    # break out if drive is stopped or shutting down
                    if not self.floppy_is_running or not self.running:
                        break
                    else:
                        # pick one at random
                        play_obj = dot[random.randint(0, 3)].play()
                        play_obj.wait_done()


    def run_floppy(self, flag):
        """Run or stop the floppy drive sound effects

        Augment your user experience with the industrial melodies of a 
        1980s PC floppy drive

        Args:
            flag (boolean): True to run the drive, False to stop

        """

        self.floppy_is_running = flag


    def boot(self, skip_welcome_screen=False):
        """Boot the Nimbus
        
        This will reveal the display screen and start all the Nimbus-related processed.  By 
        default the Nimbus will go through the Welcome Screen and a mock boot-up sequence 
        before returning control to your app.  You can bypass the Welcome Screen by passing 
        skip_welcome_screen=True.  Once boot() has been called, the Nimbus can be interrupted 
        and stopped programmatically by calling the shutdown() method, or during runtime by 
        the user pressing CTRL-C. 

        Args:
            skip_welcome_screen (bool, optional): Bypass the Welcome Screen and boot sequence
            
        """

        # Don't boot if already running
        if self.running:
            message(self.silent, 'The Nimbus is already running')
            return

        message(self.silent, 'Booting up')

        # Initialize pygame and handle full screen
        pygame.init()
        pygame.display.set_caption(self.title)
        if self.full_screen:
            # Full screen - get full screen size as display size and set pygame flags
            self.__full_screen_display_size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
            display_size = self.__full_screen_display_size
            flags = pygame.FULLSCREEN
        else:
            # Run in window - use background size as display size and set pygame flags
            display_size = self.BACKGROUND_SIZE
            flags = 0
        self.__pygame_display = pygame.display.set_mode(display_size, flags=flags)

        # Set flags
        self.running = True

        # Start display loop in a thread
        self.__display_thread = threading.Thread(target=self.__display_loop, args=())
        self.__display_thread.start()
        # Fire up cursor in another thread
        self.__cursor_thread = threading.Thread(target=self.__cycle_cursor_flash, args=())
        self.__cursor_thread.start()
        # Fire up the floppy disk effects in another
        self.__floppy_thread = threading.Thread(target=self.__floppy_drive_effects, args=())
        self.__floppy_thread.start()
        # Fire up the keyboard listener
        self.__keyboard_listener = keyboard.Listener(
            on_press=self.__on_key_press,
            on_release=self.__on_key_release)
        self.__keyboard_listener.start()

        if skip_welcome_screen:
            # don't bother with welcome screen
            Command(self).set_mode(80)
            message(self.silent, 'Done')
            return
        else:
            # roll the welcome screen
            welcome(Command(self), self)
            Command(self).set_mode(80)
            message(self.silent, 'Done')
    

    def shutdown(self):
        """Shut down the Nimbus
        
        Stops all commands from executing, stops all Nimbus-related processes,
        closes the display window and halts program execution.

        """

        # Passshutdown if not running
        if not self.running:
            return

        message(self.silent, 'Shutting down')

        # Set flags
        self.running = False

        # Join threads
        self.__display_thread.join()
        self.__cursor_thread.join()

        # Stop keyboard listener
        self.__keyboard_listener.stop()

        # Quit pygame and exit
        pygame.quit()
        sys.exit(1)


    def sleep(self, sleep_time):
        """Pause execution like time.sleep()

        Unlike time.sleep(), this built-in sleep method will be interrupted
        if the user hits CTRL-C.  Sleep time measured in seconds.

        """

        # Validate params
        assert isinstance(sleep_time, (int, float)), "The value of sleep_time must be an integer or float, not {}".format(type(sleep_time))
        assert sleep_time > 0.01, "The value of sleep_time must be > 0.01, not {}".format(sleep_time)

        # Take 10 ms sleeps until sleep_time is reached
        # and check after each sleep if the Nimbus is still running
        elapsed_time = 0
        while elapsed_time <= sleep_time and self.running:
            if not self.running:
                break
            time.sleep(0.01)
            elapsed_time += 0.01
        return