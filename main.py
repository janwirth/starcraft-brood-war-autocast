from pynput.mouse import Button
from pynput.keyboard import Key, Listener
import pynput.mouse
import pynput.keyboard
import time

mouse = pynput.mouse.Controller()
keyboard = pynput.keyboard.Controller()

def on_press(key):
    try:
        if key.char == 'a':
            time.sleep(0.15)
            mouse.press(Button.left)
            mouse.release(Button.left)
        if key.char == 'r':
            mouse.press(Button.right)
            mouse.release(Button.right)
    except AttributeError:
        return True

def on_release(key):
    return True
#    try:
#        if key.char == 'a':
#            print('attack')
#            mouse.release(Button.left)
#        if key.char == 'r':
#            print('move')
#            mouse.release(Button.right)
#    except AttributeError:
#        return True
#    if key == Key.esc:
#        # Stop listener
#        return False

# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
