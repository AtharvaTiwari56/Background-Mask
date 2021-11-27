import cv2
import numpy as np
import time

cam = cv2.VideoCapture(0)

bgimg =cv2.imread('./img.jpg')

while cam.isOpened():
    ret, current_frame = cam.read()
    if ret:
        hsv_img = cv2.cvtColor(current_frame, cv2.COLOR_BGR2HSV)

        #lower range color
        l_black = np.array([46, 46, 46])
        u_black = np.array([33, 33, 33])
        mask1 = cv2.inRange(hsv_img, l_black, u_black)

        #upper range color
        l_black = np.array([0, 0,0])
        u_black = np.array([0,0,0])
        mask2 = cv2.inRange(hsv_img, l_black, u_black)

        full_mask = mask1+mask2

        part1 = cv2.bitwise_and(bgimg, bgimg, mask=full_mask)

        part2 = cv2.bitwise_not(full_mask)

        full_part = cv2.bitwise_and(current_frame, current_frame, mask = part2)

        cv2.imshow('wow', part1 + full_part)


cam.release()
cv2.destroyAllWindows()