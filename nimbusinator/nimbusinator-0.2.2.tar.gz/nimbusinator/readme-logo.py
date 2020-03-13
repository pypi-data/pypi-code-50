import time
from nimbusinator import Nimbus, Command

if __name__ == '__main__':
    nim = Nimbus()
    cmd = Command(nim)
    nim.boot(skip_welcome_screen=True)
    cmd.set_mode(40)
    cmd.set_paper(9)
    cmd.cls()
    title = 'Nimbusinator'
    x = 10
    y = 50
    for d in [-1, 0, 1]:
        cmd.plot(title, (x+d, y-d), size=3, brush=0)
        cmd.plot(title, (x-d, y+d), size=3, brush=0)
        cmd.plot(title, (x, y-d), size=3, brush=0)
        cmd.plot(title, (x, y+d), size=3, brush=0)
        cmd.plot(title, (x+d, y), size=3, brush=0)
        cmd.plot(title, (x-d, y), size=3, brush=0)
    cmd.plot(title, (x, y), size=3, brush=15)
    time.sleep(10)
    nim.shutdown()