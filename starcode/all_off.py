from star import Star
from time import sleep

star = Star()

try:
    star.off()
    while True:
        sleep(.5)
except KeyboardInterrupt:
    star.close()
