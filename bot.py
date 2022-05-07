from cv2 import COLOR_BAYER_BG2GRAY
import keyboard
import pyautogui
import cv2
import time

x, y, w, h = 661, 318, 194, 63 #Camera dimensions
objects = ["imgs/Cactus5.png", "imgs/Char1.png", "imgs/Cactus6.png", "imgs/Cactus7.png"]
player = cv2.imread("imgs/Player.png")

def getDistance(img):
    pass

#action inputs
def jump():
    keyboard.press('space')
    time.sleep(0.2)
    keyboard.release('space')

def crouch(seconds):
    keyboard.press("down")
    time.sleep(seconds)
    keyboard.release("down")

#Execution
def Run():
    while not keyboard.is_pressed('esc'):
        pyautogui.screenshot("imgs/screen.png", (x,y,w,h))
        image_gray = cv2.cvtColor(cv2.imread("imgs/screen.png"), cv2.COLOR_BGR2GRAY)
        
        for img_input in objects:
            object = cv2.imread(img_input)
            temp_gray = cv2.cvtColor(object, cv2.COLOR_RGB2GRAY)
            #tempWidth, tempHeight = temp_gray.shape[::-1] --will be used later
            matchResult = cv2.matchTemplate (
                image = image_gray,
                templ = temp_gray,
                method = cv2.TM_CCOEFF_NORMED
            )
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(matchResult)
            if max_val >= 0.7:
                #differentiate between cactus and pterodactyl
                if img_input == "imgs/Char1.png" and max_loc[1] >= 336:
                    crouch(0.6)
                else:
                    jump()
                    time.sleep(0.1)  #fast-landing strategy until proper prediction method is implemented
                    crouch(0.2)
        
                
            
