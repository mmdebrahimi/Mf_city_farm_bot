import cv2 as cv
#import numpy as np
import os
from time import time, sleep
from windowcapture import WindowCapture
from vision import Vision
#import win32api, win32con
import pyautogui as pg
from PIL import Image
import pyautogui
from threading import Thread
# from vision.Vision import apply_hsv_filter

#use this code to train model - you can change the numStages value to do more epochs but don't overfit!
# C:\Users\MohammadEbrahimieshr\Downloads\opencv\build\x64\vc15\bin\opencv_traincascade.exe -data C:\Users\MohammadEbrahimieshr\PycharmProjects\Mf_city_farm_bot1\ -vec pos.vec -bg neg.txt -w 24 -h 24 -precalcValBufSize 6000 -precalcIdxBufSize 6000 -numPos 800 -numNeg 400 -numStages 20 -maxFalseAlarmRate 0.3 -minHitRate 0.999

print("Monitor size: ", pg.size())
# Change the working directory to the folder this script is in.
# Doing this because I'll be putting the files from each video in their own folder on GitHub
os.chdir(os.path.dirname(os.path.abspath(__file__)))


# initialize the WindowCapture class
wincap = WindowCapture('BlueStacks')

#load the model
cascade_resources = cv.CascadeClassifier('cascade.xml')
#load an empty vision class
vision_rss = Vision(None)

#this global variable is used to notify the main loop of when the bot actions have completed
is_bot_in_action = False

def bot_actions(rectangles):
    # take bot actions
    if len(rectangles) > 0:
        # just grab the first objects detection in the list and find the place to click
        targets = Vision.get_click_points(rectangles)
        print("TARGETS:", targets, type(targets[0]))
        target = wincap.get_screen_position(targets)
        pyautogui.moveTo(x=target[0], y=target[1])
        pyautogui.click()
        # #wait 5 sec for bot action to stop
        sleep(5)
    # is_bot_in_action: bool #when this process is complete
    global is_bot_in_action
    is_bot_in_action = False

# vision_cash = Vision('cash6.jpg')
#
# # initialize the Vision class
# vision_cash = Vision('cash6.jpg')
# vision_cargo = Vision('cargo1.jpg')
# vision_metal = Vision('metal.jpg')
# vision_ammo = Vision('ammo.jpg')
#
# vision_cash.init_control_gui()
# vision_cargo.init_control_gui()
# vision_metal.init_control_gui()
# vision_ammo.init_control_gui()


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



# press 'q' with the output window focused to exit.
# waits 1 ms every loop to process key presses
while(True):
    # get an updated image of the game
    screenshot = wincap.get_screenshot()

    # implement the object detection
    rectangles = cascade_resources.detectMultiScale(screenshot)
    #points = vision_gunsnbottle.find(screenshot, 0.7, 'points')


#
#    print(x_coord[0])
#    click ()
# # =============================================================================
# #     if timer == 0:
# #
# #         click(points[0][0], points[0][1])
# #         timer = timer + 300
# # =============================================================================
#

    # rectangles = vision_cash.find(screenshot, 0.41)

#     # display the processed image
#     rectangles1 = vision_cash.find(screenshot, 0.41)
#
#     # display the processed image
#     rectangles2 = vision_cargo.find(screenshot, 0.46)
# #    print(points.split(*points[0]))
#
#     pg.moveTo()#??dafuq is this for?
#     # display the processed image
#     rectangles3 = vision_metal.find(screenshot, 0.41)
#
#      # display the processed image
#     rectangles4 = vision_ammo.find(screenshot, 0.41)
    # if bool(points1):
    #     print(points1[0][0])
    detection_image = vision_rss.draw_rectangles(screenshot, rectangles)

    # output_image1 = vision_cash.draw_rectangles(screenshot, rectangles1)
    # output_image2 = vision_cargo.draw_rectangles(screenshot, rectangles2)
    # output_image3 = vision_metal.draw_rectangles(screenshot, rectangles3)
    # output_image4 = vision_ammo.draw_rectangles(screenshot, rectangles4)


    # #Apply the HSV filter
    # output_image1 = output_image1.apply_hsv_filter(screenshot)
    # output_image2 = output_image2.apply_hsv_filter(screenshot)
    # output_image3 = output_image3.apply_hsv_filter(screenshot)
    # output_image4 = output_image4.apply_hsv_filter(screenshot)


    # output_imageA = cv.addWeighted(output_image1, 0.5, output_image2, 0.5, 0)
    # output_imageB = cv.addWeighted(output_image3, 0.5, output_image4, 0.5, 0)
    # # global output_image_final
    # output_image_final = cv.addWeighted(output_imageA, 0.5, output_imageB, 0.5, 0)
    # # output_image_final = scipy.misc.toimage(output_image_final)
    # output_image = Image.fromarray(output_image_final)
    # output_image = output_image_final.apply_hsv_filter(screenshot)
    # cv.imwrite('BlendedImage.jpg', output_image)

    #display the processed image
    cv.imshow('Matches', detection_image)

    #only start bot action if another action is not being done to avoid overloading the system with actions
    #Using multi threading in order to seperate image recognition processing and bot action processing
    if not is_bot_in_action:
        is_bot_in_action = True
        t = Thread(target = bot_actions, args = (rectangles,))
        t.start()

    # print('Cash: ', rectangles1, 'Cargo: ', rectangles2, 'Metal: ', rectangles3, 'Ammo: ', rectangles4)
    # debug the loop rate
    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()
    for coordinates in rectangles:
        print(coordinates)
    key = cv.waitKey(1)
    if key == ord('q'):
        cv.destroyAllWindows()
        break
    elif key == ord('f'):
        cv.imwrite('positive/{}.jpg'.format(loop_time), screenshot)
    elif key == ord('d'):
        cv.imwrite('negative/{}.jpg'.format(loop_time), screenshot)

print('Done.')


#
# print('Done.')
