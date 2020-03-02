from pynput.keyboard import Key, Listener, KeyCode, Controller

# Special Characters

# ASCII characters found at https://donsnotes.com/tech/charsets/ascii.html

control_characters = {  'a':'\\x01', 'b':'\\x02', 'c':'\\x03',
                        'd':'\\x04', 'e':'\\x05', 'f':'\\x06',
                        'g':'\\x07', 'h':'\\x08', 'i':'\\x09',
                        'j':'\\x0a', 'k':'\\x0b', 'l':'\\x0c',
                        'm':'\\x0d', 'n':'\\x0e', 'o':'\\x0f',
                        'p':'\\x10', 'q':'\\x11', 'r':'\\x12',
                        's':'\\x13', 't':'\\x14', 'u':'\\x15',
                        'v':'\\x16', 'w':'\\x17', 'x':'\\x18',
                        'y':'\\x19', 'z':'\\x1a', '[':'\\x1b',
                        ']':'\\x1d', '^':'\\x1e', '_':'\\x1f',
                        '?':'\\x7f', 'caps_lock': 'caps_lock'}

alt_characters = {      'a':'<65>', 'b':'<66>', 'c':'<67>',
                        'd':'<68>', 'e':'<69>', 'f':'<70>',
                        'g':'<71>', 'h':'<72>', 'i':'<73>',
                        'j':'<74>', 'k':'<75>', 'l':'<76>',
                        'm':'<77>', 'n':'<78>', 'o':'<79>',
                        'p':'<80>', 'q':'<81>', 'r':'<82>',
                        's':'<83>', 't':'<84>', 'u':'<85>',
                        'v':'<86>', 'w':'<87>', 'x':'<88>',
                        'y':'<89>', 'z':'<90>', '[':'<91>',
                        '\\':'<92>', ']':'<93>', '^':'<94>',
                        '_':'<95>', '?':'<63>', 'caps_lock': 'caps_lock'}

# Functions

current_key = None

is_special_key_pressed = {'ctrl':False, 'shift':False, 'alt':False, 'cmd':False}

recent_input = []

def value(key):
    try:
        return key.char
    except AttributeError:
        return str(key).replace('Key.', '')

def key_string(key):
    key = str(KeyCode.from_char(key))
    key = key.replace('Key.', '').replace('"','')
    key = eval(key)
    return key

def release_all_special_keys():
    keyboard = Controller()
    special_keys = [Key.ctrl_l, Key.ctrl_r, Key.ctrl, Key.shift, Key.shift_r, Key.alt, Key.alt_l, Key.alt_r]
    for key in special_keys:
        keyboard.release(key)

def activate_special_key_if_pressed(key):
    global is_special_key_pressed
    if value(key) == 'ctrl_l' or value(key) == 'ctrl_r':
        is_special_key_pressed['ctrl'] = True
    elif value(key) == 'shift' or value(key) == 'shift_r':
        is_special_key_pressed['shift'] = True
    elif value(key) == 'alt_l' or value(key) == 'alt_r':
        is_special_key_pressed['alt'] = True
    elif value(key) == 'cmd' or value(key) == 'cmd_l' or value(key) == 'cmd_r':
        is_special_key_pressed['cmd'] = True

def deactivate_special_key_if_released(key):
    global is_special_key_pressed
    if value(key) == 'ctrl_l' or value(key) == 'ctrl_r':
        is_special_key_pressed['ctrl'] = False
    elif value(key) == 'shift' or value(key) == 'shift_r':
        is_special_key_pressed['shift'] = False
    elif value(key) == 'alt_l' or value(key) == 'alt_r':
        is_special_key_pressed['alt'] = False
    elif value(key) == 'cmd' or value(key) == 'cmd_l' or value(key) == 'cmd_r':
        is_special_key_pressed['cmd'] = False

def combo(combination, current_key=current_key):
    special_keys = combination.special_keys
    character = combination.character
    if 'ctrl' in special_keys and 'alt' not in special_keys:
        character = control_characters[character]
    if 'ctrl' in special_keys and 'alt' in special_keys:
        character = alt_characters[character]
    if all( is_special_key_pressed[x] for x in special_keys ) and current_key == character:
        return True

combos = {}
keywords = {}

# Classes

class KeyboardListener:
    def __init__(self, combinations=combos, keywords=keywords):
        self.combos = combinations
        self.keywords = keywords

    def on_press(self, key):
        key = key_string(key)
        global current_key
        global is_special_key_pressed
        global recent_input
        recent_input.append(key)
        if len(recent_input) > 100:
            recent_input = []
        current_key = key
        activate_special_key_if_pressed(key)
        for combination in self.combos.values():
            if combo(combination, current_key):
                release_all_special_keys()
                combination.execute()
        for keyword in self.keywords.values():
            joined_recent_input = ''.join(recent_input)
            if keyword.joined_string_list in joined_recent_input:
                recent_input = []
                keyword.execute()


    def on_release(self, key):
        key = key_string(key)
        deactivate_special_key_if_released(key)
        if key == 'esc':
            return False

    def run(self, on_press = on_press, on_release = on_release):
        with Listener(
                    on_press=self.on_press,
                    on_release=self.on_release) as l:
                l.join()

class Combo:
    def __init__(self, special_keys, character, function, *args, **kwargs):
        self.special_keys = special_keys
        self.character = character
        self.function = function
        self.args = args
        self.kwargs = kwargs
    def execute(self):
        self.function(*self.args, **self.kwargs)

class KeyWord:
    def __init__(self, string, function, *args, **kwargs):
        self.string = string
        self.string_list = []
        self.string_list = ['space' if x == ' ' else x for x in self.string]
        self.joined_string_list = ''.join(self.string_list)
        self.function = function
        self.args = args
        self.kwargs = kwargs
    def execute(self):
        self.function(*self.args, **self.kwargs)
