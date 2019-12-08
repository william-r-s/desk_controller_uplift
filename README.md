# desk-controller-uplift
Small script to automatically raise my Uplift standing desk

Uses the (Uplift Connect Dongle)[https://www.upliftdesk.com/connect-dongle-by-uplift-desk/], which is just a normal BLE device. Had to do some interesting stuff to reverse engineer it (use an old version of the android app on an older android device, log the bluetooth packets, and a bit of trial and error).

First, have to pair the device to ubuntu (did via bluetooth applet). Pairing code was 000001.

gatttool
connect 90:E2:02:89:67:E0

Commands
---
For presets, seem to need to send the same command twice in gatttool
Preset 1 (standing):
char-write-cmd 0x0025 f1f10500057e
Preset 2 (sitting):
char-write-cmd 0x0025 f1f10600067e
Press raise button:
char-write-cmd 0x0025 f1f10100017e
Press lower button:
char-write-cmd 0x0025 f1f10200027e

Single command to raise desk:
gatttool -b 90:E2:02:89:67:E0 --char-write-req -a 0x0025 -n f1f10500057e; gatttool -b 90:E2:02:89:67:E0 --char-write-req -a 0x0025 -n f1f10500057e

