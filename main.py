from pynput.mouse import Button
from pynput.keyboard import Key, Listener
import pynput.mouse
import pynput.keyboard
import time

ATTACK_HOTKEY = 'q'
MOVE_HOTKEY = 'w'

mouse = pynput.mouse.Controller()
keyboard = pynput.keyboard.Controller()

def on_press(key):
    try:
        if key.char == ATTACK_HOTKEY:
            keyboard.press('a')
            keyboard.release('a')
            time.sleep(0.15)
            mouse.press(Button.left)
            mouse.release(Button.left)
        if key.char == MOVE_HOTKEY:
            mouse.press(Button.right)
            mouse.release(Button.right)
    except AttributeError:
        return True

def on_release(key):
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
