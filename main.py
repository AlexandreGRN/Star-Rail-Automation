from screeninfo import get_monitors
from pynput import mouse
import pyautogui
import time
from pathlib import Path
import os
import time
import pydirectinput

game_path = "D:\\Mihoyo\\Star Rail\\launcher.exe"

class Player:
    State = "Not started"

import pyautogui
import time

def click_image(image_path, offset_x=0, offset_y=0, NewState=""):
    location = pyautogui.locateOnScreen(image_path, confidence=0.8, grayscale=True)
    if location is not None:
        x, y = pyautogui.center(location)
        pyautogui.click(x + offset_x, y + offset_y)
        print("Clicked on", image_path)
        Player.State = NewState


def affectation():
    pyautogui.press('escape')
    while Player.State == "Connected":
        click_image('./images/Affecation.png', NewState="In Affectation")


    while Player.State == "In Affectation":
        time.sleep(1.1)
        while pyautogui.locateOnScreen('./images/Notif.png', confidence=0.9, grayscale=True):
            print("Notif")
            click_image('./images/Notif.png', offset_x=-20, offset_y=20, NewState="In Affectation2")
            time.sleep(1.1)
            click_image('./images/Recup.png', NewState="In Affectation3")
            time.sleep(1.1)
            click_image('./images/Retry.png', NewState="In Affectation")
            time.sleep(2.3)
        pyautogui.press('escape')
        time.sleep(0.2)
        pyautogui.press('escape')
        Player.State = "Connected"

def connecting():
    while Player.State == "Deconnected":
        click_image('./images/Connect.png', offset_y=-100, NewState="Connecting")

    while Player.State == "Connecting":
        click_image('./images/Connect2.png', offset_y=-100, NewState="Connecting2")

    while Player.State == "Connecting2":
        click_image('./images/Daily_primo.png', NewState="Connected")
        if pyautogui.locateOnScreen('./images/CheckConnection.png', confidence=0.8, grayscale=True):
            Player.State = "Connected"

def condensed_resin():
    connecting()
    
    while Player.State == "Connected":
        if pyautogui.locateOnScreen('./images/CheckConnection.png', confidence=0.8, grayscale=True):
            pyautogui.press('f4')
            Player.State = "In daily Tab"
    
    while Player.State == "In daily Tab":
        click_image('./images/VirtualWorldTabIcon.png', NewState="In Virtual World Tab")
        click_image('./images/CondensedResinIcon.png', offset_x=50, NewState="In Virtual World Tab: As to confirm")
        time.sleep(0.1)
    
    while Player.State == "In Virtual World Tab":
        click_image('./images/CondensedResinIcon.png', offset_x=50, NewState="In Virtual World Tab: As to confirm")
    
    while Player.State == "In Virtual World Tab: As to confirm":
        click_image('./images/CondensedResinConfirm.png', NewState="Condensed Resin: +1")

    time.sleep(0.25)

    if Player.State == "condensed_resin: +1":
        pyautogui.press('escape')
        Player.State = "Connected"

def start_game():
    os.startfile(game_path)
    while Player.State == "Not started":
        click_image('./images/Play.png', NewState="Deconnected")

start_game()
connecting()
condensed_resin()
affectation()
