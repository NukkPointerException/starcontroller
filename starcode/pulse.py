from star import Star
from time import sleep

star = Star()

try:
    star.pulse()
    while True:
        sleep(.5)
except KeyboardInterrupt:
    star.close()
