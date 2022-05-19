# kerem inci
# 1306190041
# goruntu isleme odev-2

import cv2 as cv
import numpy as np

def prewit():
    Gx = 0
    Gy = 0
    for i in range(1,width - 1):
        for j in range(1,height - 1):
            Gx += (-(img[i-1,j-1] + img[i-1,j] + img[i-1,j + 1]) )
            Gx += (img[i+1,j-1] + img[i+1,j] + img[i+1,j + 1] )

            Gy += (-(img[i-1,j-1] + img[i,j-1] + img[i+1,j - 1]))
            Gy += (img[i-1,j+1] + img[i,j+1] + img[i+1,j + 1])

            result = abs(Gx) + abs(Gy)

            if result >= 255: #treshold degeri
                result = 255

            new_img[i][j] = result

            Gx = 0
            Gy = 0

    
    return



img = cv.imread("apple.jpg", cv.IMREAD_GRAYSCALE)
new_img = np.copy(img)
height, width= img.shape

prewit()

cv.imshow("Display window", new_img)
cv.waitKey(0)
