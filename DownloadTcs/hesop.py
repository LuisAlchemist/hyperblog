import os
import pyautogui
import time
import pygetwindow as gw
from tkinter import Tk, Label, Button, Entry

def open_fille_zilla():
    os.startfile("C:\Program Files\FileZilla FTP Client\Filezilla.exe")
    time.sleep(3)


    window = gw.getWindowsWithTitle("FileZilla")[0]
    window.activate()
    pyautogui.write('192.180.40.200') #write the IP Addrees
    pyautogui.press('tab') #press tab to write UserName
    pyautogui.write('datastorage') #write UserName
    pyautogui.press('tab') #press tab to write Password
    pyautogui.write('datadownload')
    pyautogui.press('enter') #press enter


if __name__ == "__main__":
    open_fille_zilla()