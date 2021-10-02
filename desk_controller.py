#!/usr/bin/env python3
# Send a message over serial port to standing desk controller every second that
# desktop is active (lock screen is not active)
import subprocess
import traceback
from time import sleep

screen_locked = False


def raise_desk():
    subprocess.run(
        [
            "gatttool -b 90:E2:02:89:67:E0 --char-write-req -a 0x0025 -n f1f10500057e; gatttool -b 90:E2:02:89:67:E0 --char-write-req -a 0x0025 -n f1f10500057e"
        ],
        shell=True,
    )


sleep(60)
# raise_desk()

while True:
    completed_process = subprocess.run(
        ["cinnamon-screensaver-command", "-t"], stdout=subprocess.PIPE
    )
    screen_locked_now = not (
        completed_process.stdout.strip() == b"The screensaver is not currently active."
    )
    print(screen_locked_now)
    if screen_locked_now and not screen_locked:
        print("Raising Desk")
        raise_desk()
    screen_locked = screen_locked_now
    sleep(1)
