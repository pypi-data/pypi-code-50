import gpiod
import time

chip = gpiod.chip("0")

print(f"chip name: {chip.name()}")
print(f"chip label: {chip.label()}")
print(f"number of lines: {chip.num_lines()}")

led = chip.find_line("PHY13")

config = gpiod.line_request()
config.consumer = "blink"
config.request_type = gpiod.line_request.DIRECTION_OUTPUT

led.request(config, 0)

print(f"line offset: {led.offset()}")
print(f"line name: {led.name()}")
print("line direction: " + ("input" if (led.direction()
                                        == gpiod.line.DIRECTION_INPUT) else "output"))
print("line active state: " + ("active low" if (led.active_state()
                                                == gpiod.line.ACTIVE_LOW) else "active high"))

while True:
    led.set_value(0)
    time.sleep(1)
    led.set_value(1)
    time.sleep(1)
