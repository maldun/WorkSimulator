import win32api, win32con
from msvcrt import getch, kbhit

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
#click(10,10)

def move(x,y):
    win32api.SetCursorPos((x,y))
    #win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,x,y,0,0)
    #win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,x,y,0,0)

import random
def random_coordinate(scale=2,offset = 500):
    number = random.randint(offset,offset*scale)
    return number
def random_event():
    return random.randint(0,2)

import time
while True:
    
    time.sleep(0.1)
    
    X = random_coordinate()
    Y = random_coordinate()
    if random_event():
        click(X,Y)
    else:
        move(X,Y)
    
    if kbhit():
        key = ord(getch())
        if key == 27: #ESC
            break
