# kerem inci
# 1306190041
# goruntu isleme odev-2

import cv2 as cv
import numpy as np
import math

def robert():
    Gx = 0
    Gy = 0
    for i in range(1,width - 1):
        for j in range(1,height - 1):
            Gx += (img[i,j] - img[i+1,j+1])
            Gy += (-img[i+1,j] + img[i,j+1])

            result = int(math.sqrt((abs(Gx**2) + abs(Gy**2))))

            if result >= 100:
                result = 255

            new_img[i][j] = result

            Gx = 0
            Gy = 0

    
    return




img = cv.imread("apple.jpg", cv.IMREAD_GRAYSCALE)
new_img = np.copy(img)
height, width= img.shape

robert()

cv.imshow("Display window", new_img)
cv.waitKey(0)
