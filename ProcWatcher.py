# from pynput import keyboard
import psutil
import os

cmd = 'python3 /Users/greg/Documents/AppDev/DailyDefinition/DailyDefinition.py'
## Find programs running
def getProcessInfo():
    bashCount = 0
    tempBashCount = 0
    for process in psutil.process_iter():
        with process.oneshot():
            name = process.name()
            if name is 'bash':
                tempBashCount += 1
    if tempBashCount == bashCount or tempBashCount < bashCount:
        return
    if tempBashCount > bashCount:
        os.system(cmd)
                

## Keyboard listener - temp?
# def on_press(key):
#     try:
#         print('alphanumeric key {0} pressed'.format(key.char))
#     except AttributeError:
#         print('special key {0} pressed'.format(key))

# def on_release(key):
#     print('{0} released'.format(key))
#     if key == keyboard.Key.esc:
#         return False

# with keyboard.Listener(
#         on_press=on_press,
#         on_release=on_release) as listener:
#     listener.join()
# getProcessInfo()

