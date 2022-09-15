#!/usr/bin/env python3

from typing import Dict
from pynput.mouse import Button
from pynput.keyboard import Key, Listener, KeyCode
import pynput.mouse
import pynput.keyboard
import time

ATTACK_HOTKEY = 'f'
RMB_HOTKEY = 'w'
LMB_HOTKEY = 'q'

mouse = pynput.mouse.Controller()
keyboard = pynput.keyboard.Controller()

pressed: Dict[str, bool] = {}

def on_press(key: KeyCode):

    try:
        if (not (key.char)):
            return
        if pressed.get(key.char):
            return
        print("CURRENT", pressed, pressed.get(key.char))
        pressed[key.char] = True
        print("PRESS", key )
        if key.char == ATTACK_HOTKEY:
            keyboard.press('a')
            keyboard.release('a')
            time.sleep(0.15)
            mouse.press(Button.left)
            time.sleep(0.05)
            mouse.release(Button.left)
        if key.char == LMB_HOTKEY:
            mouse.press(Button.left)
        if key.char == RMB_HOTKEY:
            mouse.press(Button.right)
    except AttributeError:
        return True

def on_release(key: KeyCode):
    try:
        print("RELEAESE", key )
        if not key.char:
            return
        time.sleep(0.15)
        pressed[key.char] = False
        if key.char == LMB_HOTKEY:
            mouse.release(Button.left)
        if key.char == RMB_HOTKEY:
            mouse.release(Button.right)
    except:
        pass
    return True
#    try:
#        if key.char == ATTACK_HOTKEY:
#            mouse.release(Button.left)
#        if key.char == MOVE_HOTKEY:
#            mouse.release(Button.right)
#    except AttributeError:
#        return True

# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release
    ) as listener:
    listener.join()
