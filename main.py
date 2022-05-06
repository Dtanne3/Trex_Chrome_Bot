#https://www.tuckercraig.com/dino/

import keyboard
import bot

if __name__ == "__main__":
    print("press '[' to start. press ']' to cancel")
    while True:
        if keyboard.is_pressed('[') == True:
            bot.Run()
            break
        elif keyboard.is_pressed(']') == True:
            print("exiting..")
            break