# Detergent's TFT Bot
# Branch: main

import pkg_resources
import pyautogui as auto
from python_imagesearch.imagesearch import imagesearch as search
import time
from printy import printy
from python_imagesearch.imagesearch import imagesearch_count as count
import Rank

print(count)
pkg_resources.require("PyAutoGUI==0.9.50")
pkg_resources.require("opencv-python==4.5.1.48")
pkg_resources.require("python-imageseach-drov0==1.0.6")

auto.FAILSAFE = False

# Start utility methods
def onscreen(path, precision=0.8):
    return search(path, precision)[0] != -1


def search_to(path):
    pos = search(path)
    if onscreen(path):
        auto.moveTo(pos)
        return pos


def click_key(key, delay=.1):
    auto.keyDown(key)
    time.sleep(delay)
    auto.keyUp(key)


def click_left(delay=.1):
    auto.mouseDown()
    time.sleep(delay)
    auto.mouseUp()


def click_right(delay=.1):
    auto.mouseDown(button='right')
    time.sleep(delay)
    auto.mouseUp(button='right')


def click_to(path, delay=.1):
    if onscreen(path):
        auto.moveTo(search(path))
        click_left(delay)
# End utility methods



def myrank():
    position = search("./captures/MyPosition.png")
    reference = search("./captures/settings.png")
    return Rank.ingame(position, reference)

def place():
    position = search("./captures/MyRanking.png")
    reference = search("./captures/play again.png")
    return Rank.postgame(position, reference)
      
# Start main process
def main():
    
    tokens = 0
    surrenderflag = False
    while True:
        if onscreen("./captures/settings.png"):
            if onscreen("./captures/reconnect.png"):
                print("reconnecting!")
                time.sleep(0.5)
                click_to("./captures/reconnect.png") 
            if onscreen("./captures/dead.PNG"):
                click_to("./captures/dead.PNG")     
            if onscreen("./captures/3-4.png"):
                surrenderflag = True
            
            if  surrenderflag == True:
                zeros = count("./captures/zero hp.png")
                rank = myrank();
                if ((rank - zeros) == 1) and onscreen("./captures/lose streak.PNG"):    #Surrender when last and lose streak
                    surrender()
                if zeros == 6:                                                          #Surrender when  2 place
                    surrender()          
            time.sleep(10)
            
        else:
            if onscreen("./captures/find match ready.png"):
                click_to("./captures/find match ready.png")
                surrenderflag = False
                print("Queued up!")              
            if onscreen("./captures/accept.png"):
                click_to("./captures/accept.png")
                print("Match accepted!")
            if onscreen("./captures/missions ok.png"):
                click_to("./captures/missions ok.png")
            if onscreen("./captures/play again.png"):
                tokens += place()
                print("Tokens farmed  this session:", tokens)
                click_to("./captures/play again.png")
            if onscreen("./captures/skip waiting for stats.png"):
                click_to("./captures/skip waiting for stats.png")  
            time.sleep(5)


    
def surrender():
    if auto.confirm("Surrender?", timeout=5000) == "Cancel":
        surrenderflag = False
    else:
        click_to("./captures/settings.png")
        time.sleep(1)
        while not onscreen("./captures/surrender 1.png"):
            click_to("./captures/settings.png")  # just in case it gets interrupted or misses
            time.sleep(1)
        while not onscreen("./captures/surrender 2.png"):
            click_to("./captures/surrender 1.png")

        time.sleep(1)
        click_to("./captures/surrender 2.png")
        time.sleep(10) 

# End main process


# Start auth + main script
print("Developed by:")
printy(r"""
[c>] _____       _                            _   @
[c>]|  __ \     | |                          | |  @
[c>]| |  | | ___| |_ ___ _ __ __ _  ___ _ __ | |_ @
[c>]| |  | |/ _ \ __/ _ \ '__/ _` |/ _ \ '_ \| __|@
[c>]| |__| |  __/ ||  __/ | | (_| |  __/ | | | |_ @
[c>]|_____/ \___|\__\___|_|  \__, |\___|_| |_|\__|@
[c>]                          __/ |               @
[c>]                         |___/                @
[c>]    ______               __            @
[c>]   / ____/___ __      __/ /_____  _____@
[c>]  / /_  / __ `/ | /| / / //_/ _ \/ ___/@
[c>] / __/ / /_/ /| |/ |/ / ,< /  __(__  ) @
[c>]/_/    \__,_/ |__/|__/_/|_|\___/____/  @                                
[c>] ____   __    _       _     ____  ____  __  @
[c>]| |_   / /\  \ \    /| |_/ | |_  | |_  ( (` @
[c>]|_|   /_/--\  \_\/\/ |_| \ |_|__ |_|__ _)_) @
[c>]@
[c>]____ ____ _ _ _ _  _ ____ ____ ____ @
[c>]|___ |__| | | | |_/  |___ |___ [__  @
[c>]|    |  | |_|_| | \_ |___ |___ ___] @                                  
[c>]   ____            __         @
[c>]  / __/__ __    __/ /_____ ___@
[c>] / _// _ `/ |/|/ /  '_/ -_|_-<@
[c>]/_/  \_,_/|__,__/_/\_\\__/___/@                             
""")


printy(f"Welcome! You're running Detergent's TFT bot.\nPlease feel free to ask questions or contribute at https://github.com/Detergent13/tft-bot", "nB")
print("Bot started")
main()

# End auth + main script
