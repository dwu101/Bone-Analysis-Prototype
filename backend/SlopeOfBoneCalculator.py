# maybe find a guarenteed bone spot, then go up and down many many times ( within the range of the bone minus a margin) and find the slope of
# each, finding the average as you go ? this will be some interesting code to write tbh. test with the manual angle finder on the mock bone.


import cv2
import math
# import matplotlib.pyplot as plt
import numpy as np
from operator import itemgetter
# import pyautogui for screenshots

import time
# from PIL import Image

global img
# CHANGE THIS TO YOUR PATH!!!! :) or dont i think it works
img = cv2.imread(
    "/backend/bonescreenshot.jpg")


def find_edge(x, y):
    threshold = 147
    while True:  # finds the edge of the bone
        if x <= 0:
            # cv2.putText(img,"Bone not found",(50,50),2,0.5,(255,255,255),2)

            return "None"

        if (img[y, x][0] > threshold and img[y, x][1] > threshold and img[y, x][2] > threshold).any():
            if (img[y, x-1][0] > threshold and img[y, x-1][1] > threshold and img[y, x-1][2] > threshold).any():
                # cv2.circle(img, (x,y),10,(0,255,0), -1)
                return [x, y]

        x -= 1


def edge_finder(xp):

    size = img.shape
    x = size[1]
    y = size[0]
    print(x, y)

    edge_points = []
    numpix = 1
    pixaway = 1
    direction = 1
    while numpix <= 100:

        append = find_edge(x-1, y-xp + (pixaway*direction))
        if append == "None":
            direction = -1
            pixaway = 1
        else:
            edge_points.append(append)
        pixaway += 1
        numpix += 1
        if numpix == 10:
            print("x")

    print(edge_points)

    x = 1
    edge_points = (sorted(edge_points, key=itemgetter(0), reverse=True))
    while True:
        try:
            if math.fabs(edge_points[x][0] - edge_points[x-1][0]) > 2:
                del edge_points[x]
            else:
                x += 1

        except:
            break

    x = 1
    edge_points = (sorted(edge_points, key=itemgetter(1), reverse=True))
    while True:
        try:
            if math.fabs(edge_points[x][1] - edge_points[x-1][1]) > 2:
                del edge_points[x]
            else:
                x += 1

        except:
            break

    return edge_points


# this doesnt work for 10 cuz the edge is straight. figure out a work around.
def slope(points):
    for check in range(1, len(points)):
        if points[check][0] != points[check-1][0]:
            break
    else:
        return "straight"

    x = []
    y = []
    for element in points:
        x.append(element[0])
        y.append(element[1]*-1)
    x = np.array(x)
    y = np.array(y)

    a, b = np.polyfit(x, y, 1)
    # plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)))
    # plt.show()
    if a < 0:
        a *= -1
    return a


def point_drawer(points):
    global img
    for element in points:
        cv2.circle(img, (element[0], element[1]), 1, (0, 255, 0), -1)

    img2 = cv2.resize(img, (700, 800))
    while (1):
        cv2.imshow("Slope Finder", img2)
        if cv2.waitKey(0) & 0xFF == 27:
            break


def length(point1, point2):
    x_dif = point1[0] - point2[0]
    y_dif = point1[1] - point2[1]
    return math.sqrt((x_dif)**2 + (y_dif)**2)


def angle_calculator(num1, num2):
    shared_vertex = (0, 0)
    if num1 == "straight" and num2 == "straight":
        return "bones are perfectly aligned"

    elif num1 == "straight":
        point1 = (0, 1)
        point2 = (1, num2)

    elif num2 == "straight":
        point1 = (1, num1)
        point2 = (0, 1)

    else:
        point1 = (1, num1)
        point2 = (1, num2)

    line1_len = length(shared_vertex, point1)
    line2_len = length(shared_vertex, point2)
    line3_len = length(point1, point2)

    angle_rad = math.acos(
        (line1_len**2 + line2_len**2 - line3_len**2)/(2*line2_len*line1_len))
    angle_deg = round(angle_rad * 180 / math.pi, 2)
    # cv2.putText(img, "Angle: " + str(angle_deg) + "d", (10, 50),
    #             cv2.FONT_HERSHEY_COMPLEX, .5, (0, 255, 0), 1)
    # img2 = cv2.resize(img, (700, 800))
    # while (1):
    #     cv2.imshow("Slope Finder", img2)
    #     if cv2.waitKey(0) & 0xFF == 27:
    #         break

    return angle_deg


# def screenshot():
#     while True:
#         a = win32api.GetKeyState(0x11) # detects control click, starts taking screen shots
#         time.sleep (0.01)
#         if a < 0:
#             x = 1
#             while True:
#                 myScreenshot = pyautogui.screenshot() # takes about 6 pictures per second
#                 myScreenshot.save(r'C:\Users\danqw\OneDrive\Desktop\Screen.for.lab\{screenshot}_{x}.png'.format(x = x, screenshot = name ))
#                 x +=1

#                 b = win32api.GetKeyState(0x10) # detects right click

#                 if b < 0: # crops image after shift click
#                     for i in range(1,x+1):
#                         im = Image.open(r'C:\Users\danqw\OneDrive\Desktop\Screen.for.lab\{screenshot}_{x}.png'.format(x = i, screenshot = name ))

#                         left = 100
#                         top = 75
#                         right = 130
#                         bottom = 150

#                         im = im.crop((left, top, right, bottom))

#                         im.save(r'C:\Users\danqw\OneDrive\Desktop\Screen.for.lab\screenshot_{x}.png'.format(x = i))

#                     return x


# name = input("Description: ")
# x = screenshot(name)
# max_angle = 0
# for i in range(x):
#     bottom = edge_finder(2, "screenshot_{x}".format(x=x)) # PUT THE FILE LOCATION HERE
#     bottom_slope = slope(bottom)
#     top = edge_finder(10, "screenshot_{x}".format(x=x))
#     top_slope = slope(top)

#     angle = angle_calculator(bottom_slope, top_slope)
#     if angle > max_angle:
#         max_angle = angle

# print(angle)


def run_code():

    bottom = edge_finder(150)
    # print(bottom)
    # point_drawer(bottom)
    bottom_slope = slope(bottom)
    print(bottom_slope)

    top = edge_finder(350)
    # print(top)
    # point_drawer(top)
    top_slope = slope(top)
    # print(top_slope)

    angle = angle_calculator(bottom_slope, top_slope)
    return angle


# print(run_code())
# run_code()
