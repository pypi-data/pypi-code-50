import keyboard, os, time
def ctype(text, speed = 0.1):
    text = str(text)
    for x in range(0, len(text)):
        print(text[x], end='')
        time.sleep(speed)
    print()
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
def backspace(text, speed = 0.1):
    text = str(text)
    g = len(text)
    for x in range(0, len(text)):
        print(text[0:g], end='')
        time.sleep(speed)
        os.system('cls' if os.name == 'nt' else 'clear')
        g -= 1
    print()
def pressenter():
    keyboard.wait('enter')