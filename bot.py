from cv2 import COLOR_BAYER_BG2GRAY
import keyboard
import pyautogui
import cv2
import numpy as np
import time

x, y, w, h = 661, 318, 194, 63
cactus = cv2.imread("imgs/Cactus4.png")
temp_gray = cv2.cvtColor(cactus, cv2.COLOR_RGB2GRAY)
tempWidth, tempHeight = temp_gray.shape[::-1]

def Run():
    while not keyboard.is_pressed('esc'):
        pyautogui.screenshot("imgs/screen.png", (x,y,w,h))
        image = cv2.imread("imgs/screen.png")
        image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        matchResult = cv2.matchTemplate (
                image = image_gray,
                templ = temp_gray,
                method = cv2.TM_CCOEFF_NORMED
            )
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(matchResult)
        if max_val >= 0.3:
            keyboard.press('space')
            time.sleep(0.3)
            keyboard.release('space')
                
            
