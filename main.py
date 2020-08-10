import cv2 as cv
#import numpy as np
import os
from time import time
from windowcapture import WindowCapture
from vision import Vision
#import win32api, win32con
import pyautogui as pg


print("Monitor size: ", pg.size())
# Change the working directory to the folder this script is in.
# Doing this because I'll be putting the files from each video in their own folder on GitHub
os.chdir(os.path.dirname(os.path.abspath(__file__)))


# initialize the WindowCapture class
wincap = WindowCapture('BlueStacks')

# initialize the Vision class
vision_cash = Vision('cash6.jpg')
vision_cargo = Vision('cargo1.jpg')
vision_metal = Vision('metal.jpg')
vision_ammo = Vision('ammo.jpg')
 
#print ([vision_cash])
# =============================================================================
# def click(x,y):
#             win32api.SetCursorPos((x,y))
#             win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
#             win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
#             click(10,10)
# =============================================================================
timer = 0        
def countdown(timer):
    while timer:
        mins, secs = divmod(timer, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        timer -= 1
        return mins
loop_time = time()
while(True):
    
    # get an updated image of the game
    screenshot = wincap.get_screenshot()
    
    # display the processed image
    points1 = vision_cash.find(screenshot, 0.41, 'rectangles')
    #points = vision_gunsnbottle.find(screenshot, 0.7, 'points')
    

#    
#    print(x_coord[0])
#    click ()
# =============================================================================
#     if timer == 0:
#         
#         click(points[0][0], points[0][1])
#         timer = timer + 300
# =============================================================================
     
    
    
    
    # display the processed image
    points2 = vision_cargo.find(screenshot, 0.46, 'rectangles')
#    print(points.split(*points[0]))
    
    pg.moveTo()
    # display the processed image
    points3 = vision_metal.find(screenshot, 0.41, 'rectangles')
    
     # display the processed image
    points4 = vision_ammo.find(screenshot, 0.41, 'rectangles')
    print(points1[0][0])
#    print('Cash: ', points1, 'Cargo: ', points2, 'Metal: ', points3, 'Ammo: ', points4)

    for coordinates in points1:
        print(coordinates)
    # debug the loop rate
    print('FPS {}'.format(1 / (time() - loop_time)))
    

    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break



print('Done.')
