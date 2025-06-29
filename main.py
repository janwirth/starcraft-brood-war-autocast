#!/usr/bin/env python3

from typing import Dict
from pynput.mouse import Button
from pynput.keyboard import Key, Listener, KeyCode
import pynput.mouse
import pynput.keyboard
import time
from AppKit import NSWorkspace

ATTACK_HOTKEY = 'f'
RMB_HOTKEY = 'w'
LMB_HOTKEY = 'q'

mouse = pynput.mouse.Controller()
keyboard = pynput.keyboard.Controller()

pressed: Dict[str, bool] = {}

def on_press(key: KeyCode | Key | None) -> None:
    active_app = NSWorkspace.sharedWorkspace().activeApplication()
    app_name = active_app['NSApplicationName']
    if app_name != "StarCraft":
        return

    print(app_name)
    if key is None:
        return None
    if not isinstance(key, KeyCode):
        print("NOT KEYCODE", key)
        return None

    try:
        if (not (key.char)):
            return
        if pressed.get(key.char):
            return
        print("CURRENT", pressed, pressed.get(key.char))
        pressed[key.char] = True
        print("PRESS", key )
        if key.char == ATTACK_HOTKEY:
            print("ATTACK")
            keyboard.press('a')
            keyboard.release('a')
            time.sleep(0.15)
            mouse.press(Button.left)
            time.sleep(0.05)
            mouse.release(Button.left)
        if key.char.lower() == LMB_HOTKEY:
            print("LMB")
            mouse.press(Button.left)
        if key.char == RMB_HOTKEY:
            print("RMB")
            mouse.press(Button.right)
    except AttributeError:
        return None

def on_release(key: KeyCode | Key | None) -> None:
    active_app = NSWorkspace.sharedWorkspace().activeApplication()
    app_name = active_app['NSApplicationName']
    if app_name != "StarCraft":
        return
    if key is None:
        return None
    if not isinstance(key, KeyCode):
        print("NOT KEYCODE", key)
        return None

    try:
        print("RELEASE", key )
        if not key.char:
            return
        time.sleep(0.01)
        pressed[key.char] = False
        if key.char.lower() == LMB_HOTKEY:
            print("RELEASE LEFT")
            mouse.release(Button.left)
        if key.char == RMB_HOTKEY:
            print("RELEASE RIGHT")
            mouse.release(Button.right)
    except:
        pass
    return None
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
