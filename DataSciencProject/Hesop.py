import os
import pyautogui
import time
import pygetwindow as gw

os.startfile('C:\Kinco\Kinco HMIware v2.5\Kinco HMIware.exe')
time.sleep(3)


window = gw.getWindowsWithTitle("Kinco HMIware")[0]
window.activate()
pyautogui.press('enter') #press enter key